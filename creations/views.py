from django.shortcuts import render_to_response
from django.template import RequestContext


def books(request):
    template_dictionary = {}

    return render_to_response('books.html', template_dictionary,
                              context_instance=RequestContext(request))
