from django.contrib import admin

from creations.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_published',
    )


admin.site.register(Book, BookAdmin)
