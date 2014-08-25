from django.shortcuts import render_to_response
from django.template import RequestContext

from creations.models import Book


def books(request):
    books = Book.objects.all()
    template_dictionary = {
        'books': books,
    }

    return render_to_response('books.html', template_dictionary,
                              context_instance=RequestContext(request))
