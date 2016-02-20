from django.conf.urls import url

from . import views
from creations.feeds import ForTheBirdsPodcastFeed


urlpatterns = [
    url(r'^radio/$', views.radio, name='radio_url'),
    url(r'^radio/feed\.xml$', ForTheBirdsPodcastFeed(),
        name='radio_podcast_feed_url'),
    url(r'^radio/calendar/current/$', views.radio_current_calendar,
        name='radio_current_calendar_url'),
    url(r'^radio/calendar/(?P<year>\d\d\d\d)/(?P<month>\d+)/$',
        views.radio_calendar, name='radio_calendar_url'),
    url(r'^radio/program/(?P<id>\d+)/(?P<slug>.*)/$',
        views.radio_program, name='radio_program_url'),
    url(r'^radio/artwork/(?P<id>\d+)/$',
        views.radio_program_artwork, name='radio_program_artwork_url'),

    url(r'^writing/$', views.writing, name='writing_url'),
    url(r'^book/(?P<slug>.+)/$', views.book, name='book_url'),
    url(r'^article/(?P<id>\d+)/(?P<slug>.*)/$',
        views.article, name='article_url'),

    url(r'^page/(?P<slug>.+)/$', views.webpage, name='webpage_url'),
    url(r'^miscellany/$', views.miscellany, name='miscellany_url'),

    url(r'^sound-recordings/$', views.sound_recordings,
        name='sound_recordings_url'),
    url(r'^sound-recording/(?P<id>\d+)/$', views.sound_recording,
        name='sound_recording_url'),
    url(r'^sound-recording/artwork/(?P<id>\d+)/$',
        views.sound_recording_artwork,
        name='sound_recording_artwork_url'),

    url(r'^speaking/$', views.speaking, name='speaking_url'),
    url(r'^speaking/(?P<slug>.+)/$', views.speaking_program,
        name='speaking_program_url'),

    url(r'^research/$', views.research, name='research_url'),
    url(r'^research-category/(?P<id>\d+)/$', views.research_category,
        name='research_category_url'),
    url(r'^research-item/(?P<id>\d+)/$', views.research_item,
        name='research_item_url'),
]
