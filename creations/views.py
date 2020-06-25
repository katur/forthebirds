import calendar
import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Max
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from creations.models import (Article, Book, ExternalProject,
                              RadioProgram, RadioProgramRerun,
                              RadioProgramMissedDate,
                              ResearchCategory, Research, SoundRecording,
                              SpeakingProgram, WebPage)
from website.models import User


def article(request, id, slug=None):
    """
    Render the page about an article Laura has written.
    """
    article = get_object_or_404(Article, id=id)

    context = {
        'article': article,
    }
    return render(request, 'article.html', context)


def book(request, slug):
    """
    Render the page about one of Laura's books.
    """
    book = get_object_or_404(Book, slug=slug)

    context = {
        'book': book,
    }
    return render(request, 'book.html', context)


def miscellany(request):
    """
    Render the landing page for miscellaneous projects.
    """
    if request.user.is_authenticated():
        webpages = WebPage.objects.all()
    else:
        webpages = WebPage.objects.filter(is_public=True)

    externalprojects = ExternalProject.objects.all()

    context = {
        'webpages': webpages,
        'externalprojects': externalprojects,
    }
    return render(request, 'miscellany.html', context)


def radio(request):
    """
    Render the main radio page, showing radio archives by year.
    """
    all_years = RadioProgram.objects.dates('air_date', 'year')
    all_years = sorted(all_years, reverse=True)

    year = request.GET.get('year')
    if not year:
        year = all_years[0].year

    programs = RadioProgram.objects.filter(air_date__year=year)

    context = {
        'ITUNES_SUBSCRIBE_LINK': settings.ITUNES_SUBSCRIBE_LINK,
        'PATREON_LINK': settings.PATREON_LINK,
        'SITE_DOMAIN': settings.SITE_DOMAIN,
        'year': year,
        'programs': programs,
        'all_years': all_years,
    }
    return render(request, 'radio.html', context)


def radio_program(request, id, slug=None):
    """
    Render the page for a single radio program.
    """
    program = get_object_or_404(RadioProgram, id=id)

    context = {
        'SITE_DOMAIN': settings.SITE_DOMAIN,
        'program': program,
    }
    return render(request, 'radio_program.html', context)


def radio_program_artwork(request, id):
    """
    Extract the artwork from the radio program with this id.
    """
    program = get_object_or_404(RadioProgram, id=id)
    artwork = program.get_artwork()
    response = JsonResponse({'artwork': artwork})
    return response


def radio_program_count(request):
    program_count = RadioProgram.objects.count()
    response = JsonResponse({'program_count': program_count})
    return response


def radio_calendar(request, year, month):
    """
    Render the radio calendar page.
    """
    year = int(year)
    month = int(month)

    new_programs = RadioProgram.objects.filter(
        air_date__year=year, air_date__month=month)

    reruns = RadioProgramRerun.objects.filter(
        air_date__year=year, air_date__month=month)

    missed_dates = RadioProgramMissedDate.objects.filter(
        air_date__year=year, air_date__month=month)

    day_to_programs = {}

    def process_program(program, day, is_rerun=False, is_missed_date=False):
        if day not in day_to_programs:
            day_to_programs[day] = []
        day_to_programs[day].append((program, is_rerun, is_missed_date))

    for program in new_programs:
        day = program.air_date.day
        process_program(program, day)

    for rerun in reruns:
        day = rerun.air_date.day
        process_program(rerun.program, day, is_rerun=True)

    for missed_date in missed_dates:
        day = missed_date.air_date.day
        process_program(missed_date, day, is_missed_date=True)

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
        'SITE_DOMAIN': settings.SITE_DOMAIN,
        'year': year,
        'month': calendar.month_name[month],
        'weekdays': weekdays,
        'calendar': radio_month,
        'previous_month_url': reverse('radio_calendar_url', args=(
            previous_year, previous_month)),
        'next_month_url': reverse('radio_calendar_url', args=(
            next_year, next_month)),
    }

    return render(request, 'radio_calendar.html', context)


def radio_current_calendar(request):
    """
    Redirect to the "current" calendar month.
    """
    today = datetime.datetime.now().date()

    most_recent_rerun = (RadioProgramRerun.objects
                         .filter(air_date__lte=today)
                         .aggregate(Max('air_date')))['air_date__max']

    most_recent_original = (RadioProgram.objects
                            .filter(air_date__lte=today)
                            .aggregate(Max('air_date')))['air_date__max']

    most_recent = max(most_recent_rerun, most_recent_original)
    return redirect(radio_calendar, most_recent.year, most_recent.month)


@login_required
def research(request):
    categories = ResearchCategory.objects.filter(parent__isnull=True)
    context = {
        'categories': categories,
    }
    return render(request, 'research.html', context)


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


def research_item(request, id):
    research_item = get_object_or_404(Research, id=id)

    if not research_item.is_public and not request.user.is_authenticated():
        raise Http404

    context = {
        'research_item': research_item,
    }
    return render(request, 'research_item.html', context)


def sound_recording(request, id):
    """
    Render the page about a single sound recording.
    """
    recording = get_object_or_404(SoundRecording, id=id)
    context = {
        'recording': recording,
    }
    return render(request, 'sound_recording.html', context)


def sound_recordings(request):
    """
    Render the page listing all sound recordings.
    """
    recordings = SoundRecording.objects.all()
    context = {
        'recordings': recordings,
    }
    return render(request, 'sound_recordings.html', context)


def sound_recording_artwork(request, id):
    """
    Extract the artwork from the sound recording with this id.
    """
    recording = get_object_or_404(SoundRecording, id=id)
    artwork = recording.get_artwork()
    response = JsonResponse({'artwork': artwork})
    return response


def speaking(request):
    laura = get_object_or_404(User, username='laura')
    programs = SpeakingProgram.objects.all()

    context = {
        'programs': programs,
        'laura': laura,
    }
    return render(request, 'speaking.html', context)


def speaking_program(request, slug):
    program = get_object_or_404(SpeakingProgram, slug=slug)

    context = {
        'program': program,
    }
    return render(request, 'speaking_program.html', context)


def webpage(request, slug):
    webpage = get_object_or_404(WebPage, slug=slug)
    context = {
        'webpage': webpage,
    }
    return render(request, 'webpage.html', context)


def writing(request):
    books = Book.objects.all()
    articles = Article.objects.all().order_by('published_by',
                                              '-date_published')
    context = {
        'books': books,
        'articles': articles,
    }
    return render(request, 'writing.html', context)
