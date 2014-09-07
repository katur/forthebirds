from django.conf.urls import patterns, url


urlpatterns = patterns(
    'website.views',
    url(r'^$', 'home', name='home_url'),
    url(r'^about-laura$', 'about', name='about_url'),
)
