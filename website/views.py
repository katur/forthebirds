from django.shortcuts import render, get_object_or_404

from website.models import User


def home(request):
    return render(request, 'home.html', {})


def about(request):
    laura = get_object_or_404(User, username='laura')
    context = {
        'laura': laura,
    }
    return render(request, 'about.html', context)
