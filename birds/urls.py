from django.conf.urls import patterns, url


urlpatterns = patterns(
    'birds.views',
    url(r'^birds/$', 'birds', name='birds_url'),
    url(r'^bird/(?P<id>\d+)/$', 'bird', name='bird_url'),
    url(r'^minnesota-birds/$', 'minnesota_birds', name='minnesota_birds_url'),
)
