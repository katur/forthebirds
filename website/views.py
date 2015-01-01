from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from website.models import User, UploadedImage


def home(request):
    return render(request, 'home.html', {})


def about(request):
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
