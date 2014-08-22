from django.shortcuts import render_to_response
from django.template import RequestContext

from birds.models import TaxonomicGroup, Species


def birdsOrder(request):
    orders = TaxonomicGroup.objects.filter(level__name='order')
    for order in orders:
        order.attach_descendants()

    template_dictionary = {
        'orders': orders,
    }

    return render_to_response('birdsOrder.html', template_dictionary,
                              context_instance=RequestContext(request))


def birdsSpecies(request):
    species = Species.objects.all()
    for s in species:
        s.attach_ancestors()

    template_dictionary = {
        'species': species,
    }

    return render_to_response('birdsSpecies.html', template_dictionary,
                              context_instance=RequestContext(request))
