from django.shortcuts import render, get_object_or_404

from waystohelp.models import WayToHelp


def ways_to_help(request):
    ways_to_help = WayToHelp.objects.all()

    context = {
        'ways': ways_to_help,
    }

    return render(request, '101waystohelpbirds.html', context)


def way_to_help(request, id):
    way_to_help = get_object_or_404(WayToHelp, id=id)

    context = {
        'way': way_to_help,
    }

    return render(request, 'waytohelpbirds.html', context)
