from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404

from utils.http import http_response_ok
from website.models import User, UploadedImage, PatreonThankYou

SLIDESHOW_IMAGES = (
    'https://farm9.staticflickr.com/8377/8443224020_906862b207_b.jpg',
    'https://farm6.staticflickr.com/5602/15596254576_5216a28c1c_b.jpg',
    'https://farm4.staticflickr.com/3819/9127344519_9ff6039003_b.jpg',
    'https://farm3.staticflickr.com/2943/15443275435_f8e6e0ca79_b.jpg',
    'https://farm9.staticflickr.com/8118/8705949874_b848716501_b.jpg',
    'https://farm4.staticflickr.com/3126/3128156539_410c815f3c_b.jpg',
    'https://farm4.staticflickr.com/3446/3904449304_1fef884402_b.jpg',
    'https://farm5.staticflickr.com/4102/4770673361_f3883fbb77_b.jpg',
    'https://farm9.staticflickr.com/8537/8697779098_068fe2969a_b.jpg',
    'https://farm8.staticflickr.com/7285/8733022782_e81d3b137d_b.jpg',
)


def home(request):
    """Render the homepage."""
    patreon_thank_yous = PatreonThankYou.objects.order_by('text')
    context = {
        'PATREON_LINK': settings.PATREON_LINK,
        'slideshow_images': SLIDESHOW_IMAGES,
        'patreon_thank_yous': patreon_thank_yous,
    }
    return render(request, 'home.html', context)


def about(request):
    """Render the About Laura page."""
    laura = get_object_or_404(User, username='laura')
    context = {
        'laura': laura,
    }
    return render(request, 'about.html', context)


@login_required
def uploaded_images(request):
    images = UploadedImage.objects.filter(user=request.user).order_by(
        '-time_uploaded')
    context = {'images': images}
    return render(request, 'uploaded_images.html', context)


def try_old_website(request, path):
    """
    Before returning a 404 page not found, check if path is at old website.
    """
    url = settings.OLD_SITE_DOMAIN + '/' + path

    if http_response_ok(url):
        return HttpResponsePermanentRedirect(url)
    else:
        raise Http404
