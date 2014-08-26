from django.conf.urls import patterns, url


urlpatterns = patterns(
    'creations.views',
    url(r'^books$', 'books', name='books_url'),
    url(r'^radio$', 'radio', name='radio_url'),
)
