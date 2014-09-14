from django.contrib import admin

from creations.models import (Book, Article, BlogPost, RadioProgram,
                              Research, ResearchCategory)


creation_id_fields = ('title', 'description',)
creation_tagging_fields = ('species', 'tags',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published',)

    filter_horizontal = ('species',)

    fieldsets = (
        (None, {
            'fields': creation_id_fields
        }),
        ('Publishing Info', {
            'fields': ('publisher', 'isbn_10', 'isbn_13', 'date_published',
                       'purchase_url', 'photo',),
        }),
        ('Tagging', {
            'fields': creation_tagging_fields
        }),
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'published_by')

    filter_horizontal = ('species',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)

    filter_horizontal = ('species',)


class RadioProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'original_air_date',)

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


class ResearchCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'research_category', 'attribution', 'date',
                    'url',)

    list_filter = ('research_category',)

    filter_horizontal = ('species',)

    search_fields = ('title', 'attribution', 'description',)


admin.site.register(Book, BookAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(RadioProgram, RadioProgramAdmin)
admin.site.register(ResearchCategory, ResearchCategoryAdmin)
admin.site.register(Research, ResearchAdmin)
