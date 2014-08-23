from django.shortcuts import render_to_response
from django.template import RequestContext

from birds.models import TaxonomicGroup, Species


def birds(request):
    species = Species.objects.raw(
        'SELECT species.id, species.name, species.common_name, '
        'G.name AS genus_name, '
        'S.name AS subfamily_name, '
        'F.name AS family_name, '
        'O.name AS order_name '
        'FROM birds_species AS species '
        'LEFT JOIN birds_taxonomicgroup AS G '
        'ON species.parent_id=G.id '
        'LEFT JOIN birds_taxonomicgroup AS S '
        'ON (G.parent_id=S.id AND S.level_id=3) '
        'LEFT JOIN birds_taxonomicgroup AS F '
        'ON (S.parent_id=F.id OR G.parent_id=F.id) AND F.level_id=2 '
        'LEFT JOIN birds_taxonomicgroup AS O '
        'ON F.parent_id=O.id '
        'ORDER BY species.absolute_position'
    )

    template_dictionary = {
        'species': species,
    }

    return render_to_response('birds.html', template_dictionary,
                              context_instance=RequestContext(request))
