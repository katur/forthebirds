import datetime

from django.shortcuts import redirect, render, get_object_or_404

from birds.forms import BirdSearchForm
from birds.models import Species, MinnesotaSpecies


def birds(request):
    if request.GET.get('query'):
        search_birds = []
        form = BirdSearchForm(request.GET)

        if form.is_valid():
            search_birds = form.cleaned_data['search_birds']

            if len(search_birds) == 1:
                bird_id = search_birds[0].id
                return redirect(bird, bird_id)

    else:
        form = BirdSearchForm()
        search_birds = None

    taxonomical_birds = Species.objects.raw(
        'SELECT species.id, species.scientific_name, species.common_name, '
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
        'WHERE species.is_visible = 1 '
        'ORDER BY species.absolute_position'
    )

    context = {
        'form': form,
        'search_birds': search_birds,
        'taxonomical_birds': taxonomical_birds,
    }

    return render(request, 'birds.html', context)


def minnesota_birds(request):
    birds = MinnesotaSpecies.objects.filter(include_in_book=True)
    context = {'birds': birds}
    return render(request, 'minnesota_birds.html', context)


def bird(request, slug):
    def organize_creations(creations):
        mindate = datetime.date(datetime.MINYEAR, 1, 1)

        def get_sorting_date(x):
            return x.get_display_date() or mindate

        def get_name(x):
            return x.get_class_display_name()

        creations = sorted(creations, key=get_sorting_date, reverse=True)
        creations = sorted(creations, key=get_name)
        return creations

    bird = get_object_or_404(Species, slug=slug)

    bird.is_minnesotan = hasattr(bird, 'minnesotaspecies')

    public_creations = []
    private_creations = []

    for creation in bird.creation_set.all():
        # Get actual instances to take advantage of polymorphic fields
        actual_creation = creation.get_actual_instance()

        if actual_creation.is_public:
            public_creations.append(actual_creation)
        elif request.user.is_authenticated():
            private_creations.append(actual_creation)
        else:
            continue

    public_creations = organize_creations(public_creations)
    private_creations = organize_creations(private_creations)

    context = {
        'bird': bird,
        'public_creations': public_creations,
        'private_creations': private_creations,
    }

    return render(request, 'bird.html', context)
