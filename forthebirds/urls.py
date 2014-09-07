from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('website.urls')),
    url(r'', include('birds.urls')),
    url(r'', include('creations.urls')),
    url(r'', include('waystohelp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
