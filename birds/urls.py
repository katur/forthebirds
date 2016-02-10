from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^birds/$', views.birds, name='birds_url'),
    url(r'^photo-checklist/$', views.photo_checklist,
        name='photo_checklist_url'),
    url(r'^bird/(?P<slug>.+)/$', views.bird, name='bird_url'),
]
