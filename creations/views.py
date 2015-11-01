import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from creations.models import (RadioProgram, RadioProgramRerun,
                              Book, Article,
                              WebPage, ExternalProject,
                              SpeakingProgram, SpeakingProgramFile,
                              ResearchCategory, Research)
from website.models import User


def radio(request):
    year_list = RadioProgram.objects.all().dates('original_air_date',
                                                 'year')
    year_list = sorted(year_list, reverse=True)
    programs = RadioProgram.objects.all()
    context = {
        'programs': programs,
        'year_list': year_list,
    }
    return render(request, 'radio.html', context)


def radio_program(request, id):
    program = get_object_or_404(RadioProgram, id=id)

    context = {
        'program': program,
    }
    return render(request, 'radio_program.html', context)


def radio_calendar(request, year, month):
    program_air_dates = RadioProgramRerun.objects.filter(
        date__year=year, date__month=month)

    context = {
        'year': year,
        'month': month,
        'program_air_dates': program_air_dates,
    }

    return render(request, 'radio_calendar.html', context)


def radio_current_calendar(request):
    today = datetime.datetime.now().date()
    current = (RadioProgramRerun.objects.filter(
        date__lte=today)
        .aggregate(Max('date')))['date__max']
    print current
    return redirect(radio_calendar, current.year, current.month)


def writing(request):
    books = Book.objects.all()
    articles = Article.objects.all()
    context = {
        'books': books,
        'articles': articles,
    }
    return render(request, 'writing.html', context)


def book(request, id):
    book = get_object_or_404(Book, id=id)

    context = {
        'book': book,
    }
    return render(request, 'book.html', context)


def article(request, id):
    article = get_object_or_404(Article, id=id)

    context = {
        'article': article,
    }
    return render(request, 'article.html', context)


def speaking(request):
    laura = get_object_or_404(User, username='laura')
    programs = SpeakingProgram.objects.all()

    context = {
        'programs': programs,
        'laura': laura,
    }
    return render(request, 'speaking.html', context)


def speaking_program(request, id):
    program = get_object_or_404(SpeakingProgram, id=id)
    if request.user.is_authenticated() and request.user.is_staff:
        files = SpeakingProgramFile.objects.filter(program=program)
    else:
        files = None

    context = {
        'program': program,
        'files': files,
    }
    return render(request, 'speaking_program.html', context)


def miscellany(request):
    webpages = WebPage.objects.all()
    externalprojects = ExternalProject.objects.all()
    context = {
        'webpages': webpages,
        'externalprojects': externalprojects,
    }
    return render(request, 'miscellany.html', context)


def webpage(request, slug):
    webpage = get_object_or_404(WebPage, slug=slug)
    context = {
        'webpage': webpage,
    }
    return render(request, 'webpage.html', context)


@login_required
def all_research(request):
    categories = ResearchCategory.objects.filter(parent__isnull=True)
    context = {
        'categories': categories,
    }
    return render(request, 'all_research.html', context)


@login_required
def research_category(request, id):
    category = get_object_or_404(ResearchCategory, id=id)
    children_categories = ResearchCategory.objects.filter(parent=category)
    children_items = Research.objects.filter(category=category)
    context = {
        'category': category,
        'children_categories': children_categories,
        'children_items': children_items,
    }
    return render(request, 'research_category.html', context)


def research(request, id):
    research_item = get_object_or_404(Research, id=id)

    if not research_item.is_public and not request.user.is_authenticated():
        raise Http404

    context = {
        'research_item': research_item,
    }
    return render(request, 'research.html', context)
