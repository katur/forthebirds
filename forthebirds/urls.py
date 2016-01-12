from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from forthebirds.redirects import PERMANENT_REDIRECTS


admin.autodiscover()


urlpatterns = []


# First, redirect the annotated redirects
for old, new in PERMANENT_REDIRECTS:
    urlpatterns += [url(old, RedirectView.as_view(url=new,
                                                  permanent=False))]


urlpatterns += [
    url(r'^', include('website.urls')),
    url(r'^', include('birds.urls')),
    url(r'^', include('creations.urls')),
    url(r'^', include('waystohelp.urls')),
    url(r'^', include('private_media.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login_url'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout_url'),

    # Catchall to try old website before returning 404
    url(r'^(?P<path>.+)$', 'website.views.try_old_website'),
]
