from django.shortcuts import render, get_object_or_404

from creations.models import (Book, RadioProgram, Article,
                              ResearchCategory, Research)


def books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'books.html', context)


def radio(request):
    programs = RadioProgram.objects.all()
    context = {
        'programs': programs,
    }

    return render(request, 'radio.html', context)


def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles.html', context)


def article(request, id):
    article = get_object_or_404(Article, id=id)

    context = {
        'article': article,
    }

    return render(request, 'article.html', context)


def research_categories(request):
    categories = ResearchCategory.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'research_categories.html', context)


def research_category(request, id):
    category = get_object_or_404(ResearchCategory, id=id)
    research_items = Research.objects.filter(research_category=category)
    context = {
        'category': category,
        'research_items': research_items,
    }

    return render(request, 'research_category.html', context)


def research(request, id):
    research_item = get_object_or_404(Research, id=id)

    context = {
        'research_item': research_item,
    }

    return render(request, 'research.html', context)
