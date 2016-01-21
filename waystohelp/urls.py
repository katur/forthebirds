from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^help-birds/$', views.ways_to_help, name='ways_to_help_url'),
    url(r'^help-birds/(?P<id>\d+)/$', views.way_to_help,
        name='way_to_help_url'),
]
