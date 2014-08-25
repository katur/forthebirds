from django.conf.urls import patterns, url


urlpatterns = patterns(
    'creations.views',
    url(r'^books$', 'books', name='books_url'),
)
