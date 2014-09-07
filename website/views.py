from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from website.models import User


def home(request):
    return render_to_response('home.html', {},
                              context_instance=RequestContext(request))


def about(request):
    laura = get_object_or_404(User, username='laura')
    template_dictionary = {
        'laura': laura,
    }
    return render_to_response('about.html', template_dictionary,
                              context_instance=RequestContext(request))
