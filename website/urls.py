from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home_url'),
    url(r'^about-laura/$', views.about, name='about_url'),
]
