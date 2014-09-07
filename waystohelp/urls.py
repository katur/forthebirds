from django.conf.urls import patterns, url


urlpatterns = patterns(
    'waystohelp.views',
    url(r'^helpbirds$', 'ways_to_help', name='waystohelp_url'),
    url(r'^helpbirds/(?P<id>.+)$', 'way_to_help', name='waytohelp_url'),
)
