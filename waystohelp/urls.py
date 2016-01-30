from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^ways-to-help/$', views.ways_to_help, name='ways_to_help_url'),
    url(r'^way-to-help/(?P<id>\d+)/$', views.way_to_help,
        name='way_to_help_url'),
]
