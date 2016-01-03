from django.conf.urls import patterns, url
from creations.feeds import ForTheBirdsPodcastFeed


urlpatterns = patterns(
    'creations.views',
    url(r'^radio$', 'radio', name='radio_url'),
    url(r'^radio/podcast$', ForTheBirdsPodcastFeed(), name='podcast_url'),
    url(r'^radio/calendar/current$', 'radio_current_calendar',
        name='radio_current_calendar_url'),
    url(r'^radio/calendar/(?P<year>\d\d\d\d)/(?P<month>\d+)$',
        'radio_calendar', name='radio_calendar_url'),
    url(r'^radio/program/(?P<slug>.+)$', 'radio_program',
        name='radio_program_url'),
    url(r'^writing$', 'writing', name='writing_url'),
    url(r'^book/(?P<slug>.+)$', 'book', name='book_url'),
    url(r'^article/(?P<slug>.+)$', 'article', name='article_url'),
    url(r'^speaking$', 'speaking', name='speaking_url'),
    url(r'^speaking/(?P<slug>.+)$', 'speaking_program',
        name='speaking_program_url'),
    url(r'^page/(?P<slug>.+)$', 'webpage', name='webpage_url'),
    url(r'^miscellany$', 'miscellany', name='miscellany_url'),
    url(r'^all-research', 'all_research', name='all_research_url'),
    url(r'^research/(?P<slug>.+)$', 'research_category',
        name='research_category_url'),
    url(r'^research/(?P<category_slug>.+)/(?P<slug>.+)$', 'research',
        name='research_url'),
)
