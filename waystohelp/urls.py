from django.conf.urls import patterns, url


urlpatterns = patterns(
    'waystohelp.views',
    url(r'^101waystohelpbirds$', 'ways_to_help', name='waystohelp_url'),
    url(r'^waytohelpbirds/(?P<id>.+)$', 'way_to_help', name='waytohelp_url'),
)
