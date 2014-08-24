from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from birds.models import Species


def birds(request):
    birds = Species.objects.raw(
        'SELECT species.id, species.name, species.common_name, '
        'G.name AS genus_name, '
        'S.name AS subfamily_name, '
        'S.common_name AS subfamily_common, '
        'F.name AS family_name, '
        'F.common_name AS family_common, '
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
        'birds': birds,
    }

    return render_to_response('birds.html', template_dictionary,
                              context_instance=RequestContext(request))


def bird(request, id):
    bird = get_object_or_404(Species, id=id)

    template_dictionary = {
        'bird': bird,
    }

    return render_to_response('bird.html', template_dictionary,
                              context_instance=RequestContext(request))
