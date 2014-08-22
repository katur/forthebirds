from django.shortcuts import render_to_response
from django.template import RequestContext

from birds.models import TaxonomicGroup


def birds(request):
    orders = TaxonomicGroup.objects.filter(level__name='order')
    for order in orders:
        order.attach_descendants()

    template_dictionary = {
        'orders': orders,
    }
    return render_to_response('birds.html', template_dictionary,
                              context_instance=RequestContext(request))
