from django.conf.urls import patterns, url


urlpatterns = patterns(
    'birds.views',
    url(r'^birdsOrder$', 'birdsOrder', name='birds_url'),
    url(r'^birdsSpecies$', 'birdsSpecies'),
)
