from django.conf.urls import patterns, url


urlpatterns = patterns(
    'birds.views',
    url(r'^birds$', 'birds', name='birds_url'),
    url(r'^birds/taxonomical$', 'birds_taxonomical',
        name='birds_taxonomical_url'),
    url(r'^bird/(?P<id>.+)$', 'bird', name='bird_url'),
)
