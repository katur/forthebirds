from django.shortcuts import render, get_object_or_404

from birds.models import Species


def birds(request):
    was_search = False
    search_birds = []
    if 'query' in request.GET:
        was_search = True
        terms = request.GET['query'].split()
        birds = Species.objects.filter(is_hidden=False)
        for bird in birds:
            for term in terms:
                if (term.lower() not in bird.name.lower() and
                        term.lower() not in bird.common_name.lower()):
                    break
            else:
                search_birds.append(bird)

    context = {
        'was_search': was_search,
        'search_birds': search_birds,
    }

    return render('birds.html', context)


def birds_taxonomical(request):
    birds = Species.objects.raw(
        'SELECT species.id, species.name, species.common_name, '
        'G.name AS genus_name, '
        'S.name AS subfamily_name, '
        'S.common_name AS subfamily_common, '
        'F.name AS family_name, '
        'F.common_name AS family_common, '
        'O.name AS order_name, '
        'O.common_name AS order_common '
        'FROM birds_species AS species '
        'LEFT JOIN birds_taxonomicgroup AS G '
        'ON species.parent_id=G.id '
        'LEFT JOIN birds_taxonomicgroup AS S '
        'ON (G.parent_id=S.id AND S.level_id=3) '
        'LEFT JOIN birds_taxonomicgroup AS F '
        'ON (S.parent_id=F.id OR G.parent_id=F.id) AND F.level_id=2 '
        'LEFT JOIN birds_taxonomicgroup AS O '
        'ON F.parent_id=O.id '
        'WHERE species.is_hidden = 0 '
        'ORDER BY species.absolute_position'
    )

    context = {
        'birds': birds,
    }

    return render('birds_taxonomical.html', context)


def bird(request, id):
    bird = get_object_or_404(Species, id=id)

    context = {
        'bird': bird,
    }

    return render('bird.html', context)
