from django.contrib import admin

from creations.models import Book, RadioProgram


creation_id_fields = ('title', 'description',)
creation_tagging_fields = ('species', 'tags',)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_published',
    )

    filter_horizontal = ('species',)

    fieldsets = (
        (None, {
            'fields': creation_id_fields
        }),
        ('Publishing Info', {
            'fields': ('publisher', 'isbn_10', 'isbn_13', 'date_published',
                       'purchase_url', 'photo',),
            'classes': ('collapse',),
        }),
        ('Tagging', {
            'fields': creation_tagging_fields
        }),
    )


class RadioProgramAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'original_air_date',
    )

    filter_horizontal = ('species',)

    fieldsets = (
        (None, {
            'fields': creation_id_fields
        }),
        ('Program Details', {
            'fields': ('original_air_date', 'supplemental_content_url',
                       'transcript', 'file',),
            'classes': ('collapse',),
        }),
        ('Tagging', {
            'fields': creation_tagging_fields
        }),
    )


admin.site.register(Book, BookAdmin)
admin.site.register(RadioProgram, RadioProgramAdmin)
