from django.conf.urls import patterns, url


urlpatterns = patterns(
    'waystohelp.views',
    url(r'^help-birds$', 'ways_to_help', name='waystohelp_url'),
    url(r'^help-birds/(?P<id>.+)$', 'way_to_help', name='waytohelp_url'),
)
