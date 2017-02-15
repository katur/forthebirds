from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from website.views import try_old_website


urlpatterns = []


# First, redirect the annotated redirects
for old, new in settings.PERMANENT_REDIRECTS:
    urlpatterns += [url(old, RedirectView.as_view(url=new,
                                                  permanent=True))]


urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},
        name='login_url'),
    url(r'^logout/$', auth_views.logout, name='logout_url'),

    url(r'^', include('website.urls')),
    url(r'^(?P<path>bird\/Species\/.+)$', try_old_website),
    url(r'^(?P<path>bird\/Places\/.+)$', try_old_website),
    url(r'^', include('birds.urls')),
    url(r'^', include('creations.urls')),
    url(r'^', include('waystohelp.urls')),

    # Catchall to try old website before returning 404
    url(r'^(?P<path>.+)/$', try_old_website),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
