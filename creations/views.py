from django.shortcuts import render

from creations.models import Book, RadioProgram


def books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render('books.html', context)


def radio(request):
    programs = RadioProgram.objects.all()
    context = {
        'programs': programs,
    }

    return render('radio.html', context)
