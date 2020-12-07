import datetime

from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

from birds.forms import BirdSearchForm
from birds.models import Species


def bird(request, slug):
    """
    Render page showing a single bird species.
    """
    bird = get_object_or_404(Species, slug=slug, is_visible=True)

    public_creations = []
    private_creations = []

    for creation in bird.creation_set.select_related(
        'article',
        'blogpost',
        'book',
        'externalproject',
        'radioprogram',
        'research',
        'soundrecording',
        'speakingprogram',
        'webpage'
    ).all():
        # Get actual instances to take advantage of polymorphic fields
        actual_creation = creation.get_actual_instance()

        if actual_creation.is_public:
            public_creations.append(actual_creation)
        elif request.user.is_authenticated():
            private_creations.append(actual_creation)
        else:
            continue

    public_creations = _organize_creations(public_creations)
    private_creations = _organize_creations(private_creations)

    context = {
        'bird': bird,
        'public_creations': public_creations,
        'private_creations': private_creations,
    }

    return render(request, 'bird.html', context)


def bird_flickr_photos(request, slug):
    """
    Get the Flickr images for the bird with this slug.
    """
    bird = get_object_or_404(Species, slug=slug)
    data = bird.get_lauras_flickr_photos()
    response = JsonResponse({'data': data})
    return response


def birds(request):
    """
    Render page to find birds in various ways (search, taxonomical, etc)
    """
    if request.GET.get('query'):
        search_birds = []
        form = BirdSearchForm(request.GET)

        if form.is_valid():
            search_birds = form.cleaned_data['search_birds']

            if len(search_birds) == 1:
                this_bird = search_birds[0]
                return redirect(bird, this_bird.slug)

    else:
        form = BirdSearchForm()
        search_birds = None

    taxonomical_birds = Species.objects.filter(is_visible=True)

    context = {
        'form': form,
        'search_birds': search_birds,
        'taxonomical_birds': taxonomical_birds,
    }

    return render(request, 'birds.html', context)


def photo_checklist(request):
    """
    Render photo checklist page.
    """
    birds = (Species.objects.filter(is_visible=True)
             .exclude(main_photo_url__exact=''))

    # Shorten family common names, since using a big font
    for bird in birds:
        # Replace certain spaces with zero-width spaces, to cut down
        # width while still having line breaks behave correctly
        s = bird.family_common
        s = s.replace(', and ', u',\u200b')
        s = s.replace(', ', u',\u200b')
        s = s.replace(' and ', u',\u200b')
        bird.family_common_nospace = s

    context = {'birds': birds}
    return render(request, 'photo_checklist.html', context)


CREATION_DISPLAY_ORDER = (
    'Radio Program',
    'Sound Recording',
    'Web Page',
    'Article',
    'Blog Post',
    'Speaking Program',
    'External Project',
    'Book',
    'Research',
)


def _organize_creations(creations):
    """
    Sort creations by class type, and within that by display date (if
    available).
    """
    mindate = datetime.date(datetime.MINYEAR, 1, 1)

    def get_sorting_date(x):
        return x.get_display_date() or mindate

    def get_name(x):
        return x.get_class_display_name()

    def get_index(x):
        name = x.get_class_display_name()
        try:
            return CREATION_DISPLAY_ORDER.index(name)
        except ValueError:
            return len(CREATION_DISPLAY_ORDER)

    creations = sorted(creations, key=get_sorting_date, reverse=True)
    creations = sorted(creations, key=get_name)
    creations = sorted(creations, key=get_index)
    return creations
