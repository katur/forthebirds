from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from waystohelp.models import WayToHelp


def ways_to_help(request):
    ways_to_help = WayToHelp.objects.all()
    template_dictionary = {
        'ways': ways_to_help,
    }

    return render_to_response('101waystohelpbirds.html',
                              template_dictionary,
                              context_instance=RequestContext(request))


def way_to_help(request, id):
    way_to_help = get_object_or_404(WayToHelp, id=id)

    template_dictionary = {
        'way': way_to_help,
    }

    return render_to_response('waytohelpbirds.html', template_dictionary,
                              context_instance=RequestContext(request))
