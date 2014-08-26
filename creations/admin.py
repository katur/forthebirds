from django.contrib import admin

from creations.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'year_published',
    )


admin.site.register(Book, BookAdmin)
