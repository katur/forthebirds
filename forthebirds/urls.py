from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from forthebirds.settings import PERMANENT_REDIRECTS


urlpatterns = []


# First, redirect the annotated redirects
for old, new in PERMANENT_REDIRECTS:
    urlpatterns += [url(old, RedirectView.as_view(url=new,
                                                  permanent=False))]


urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},
        name='login_url'),
    url(r'^logout/$', auth_views.logout, name='logout_url'),

    url(r'^', include('website.urls')),
    url(r'^(?P<path>bird\/Species\/.+)$', 'website.views.try_old_website'),
    url(r'^(?P<path>bird\/Places\/.+)$', 'website.views.try_old_website'),
    url(r'^', include('birds.urls')),
    url(r'^', include('creations.urls')),
    url(r'^', include('waystohelp.urls')),
    url(r'^', include('private_media.urls')),

    # Catchall to try old website before returning 404
    url(r'^(?P<path>.+)/$', 'website.views.try_old_website'),
]
