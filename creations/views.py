import calendar
import datetime

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
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
    all_years = RadioProgram.objects.dates('air_date', 'year')
    all_years = sorted(all_years, reverse=True)

    year = request.GET.get('year')
    if not year:
        year = all_years[0].year

    programs = RadioProgram.objects.filter(air_date__year=year)

    context = {
        'year': year,
        'programs': programs,
        'all_years': all_years,
    }
    return render(request, 'radio.html', context)


def radio_program(request, id):
    program = get_object_or_404(RadioProgram, id=id)

    context = {
        'program': program,
    }
    return render(request, 'radio_program.html', context)


def radio_calendar(request, year, month):
    year = int(year)
    month = int(month)

    new_programs = RadioProgram.objects.filter(
        air_date__year=year, air_date__month=month)

    reruns = RadioProgramRerun.objects.filter(
        air_date__year=year, air_date__month=month)

    day_to_programs = {}

    def process_program(program, day, is_rerun):
        if day not in day_to_programs:
            day_to_programs[day] = []
        day_to_programs[day].append((program, is_rerun))

    for program in new_programs:
        day = program.air_date.day
        process_program(program, day, False)

    for rerun in reruns:
        day = rerun.air_date.day
        process_program(rerun.program, day, True)

    # Get a calendar that considers Sunday the first day of the week
    sunday_start = calendar.Calendar(6)

    # Get weekday names for this calendar
    weekdays = (calendar.day_name[x] for x in sunday_start.iterweekdays())

    # Iterate over reference calendar for this month (ref_month),
    # populating radio calendar for this month (radio_month) along the way
    ref_month = sunday_start.monthdayscalendar(year, month)
    radio_month = []

    for ref_week in ref_month:
        radio_week = []
        for ref_day in ref_week:
            radio_week.append((ref_day, day_to_programs.get(ref_day)))
        radio_month.append(radio_week)

    if month == 1:
        previous_month = 12
        previous_year = year - 1
    else:
        previous_month = month - 1
        previous_year = year

    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

    context = {
        'year': year,
        'month': calendar.month_name[month],
        'weekdays': weekdays,
        'calendar': radio_month,
        'previous_month_url': reverse('radio_calendar_url',
            args=(previous_year, previous_month)),
        'next_month_url': reverse('radio_calendar_url',
            args=(next_year, next_month)),
    }

    return render(request, 'radio_calendar.html', context)


def radio_current_calendar(request):
    today = datetime.datetime.now().date()

    most_recent_rerun = (RadioProgramRerun.objects
                         .filter(air_date__lte=today)
                         .aggregate(Max('air_date')))['air_date__max']

    most_recent_original = (RadioProgram.objects
                            .filter(air_date__lte=today)
                            .aggregate(Max('air_date')))['air_date__max']

    most_recent = max(most_recent_rerun, most_recent_original)
    return redirect(radio_calendar, most_recent.year, most_recent.month)


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
