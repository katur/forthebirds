from django.contrib import admin

from creations.models import (RadioProgram, RadioProgramRerun,
                              Book, Article, BlogPost,
                              WebPage, ExternalProject,
                              SpeakingProgram, SpeakingProgramFile,
                              Research, ResearchCategory)


creation_id_fields = ('title', 'description',)
creation_tagging_fields = ('species', 'tags',)


class RadioProgramRerunInline(admin.TabularInline):
    model = RadioProgramRerun


class RadioProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'air_date', 'file',)

    list_filter = ('air_date',)

    search_fields = ('title',)

    filter_horizontal = ('species',)

    fieldsets = (
        (None, {
            'fields': creation_id_fields
        }),
        ('Program Details', {
            'fields': ('air_date', 'file',
                       'supplemental_content_url', 'transcript',),
        }),
        ('Tagging', {
            'fields': creation_tagging_fields
        }),
    )

    inlines = [RadioProgramRerunInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published',)

    filter_horizontal = ('species',)

    # prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': creation_id_fields
        }),
        ('Publishing Info', {
            'fields': ('publisher', 'isbn_10', 'isbn_13', 'date_published',
                       'purchase_url', 'cover_photo'),
        }),
        ('Tagging', {
            'fields': creation_tagging_fields
        }),
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'published_by')

    filter_horizontal = ('species',)


class SpeakingProgramFileInline(admin.TabularInline):
    model = SpeakingProgramFile


class SpeakingProgramAdmin(admin.ModelAdmin):
    list_display = ('title',)

    filter_horizontal = ('species',)

    inlines = [SpeakingProgramFileInline]


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)

    filter_horizontal = ('species',)


class WebPageAdmin(admin.ModelAdmin):
    list_display = ('title',)

    filter_horizontal = ('species',)


class ExternalProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)

    filter_horizontal = ('species',)


class ResearchCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'attribution', 'date',
                    'url',)

    list_filter = ('category',)

    filter_horizontal = ('species',)

    search_fields = ('title', 'attribution', 'description',)


admin.site.register(RadioProgram, RadioProgramAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(SpeakingProgram, SpeakingProgramAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(ExternalProject, ExternalProjectAdmin)
admin.site.register(ResearchCategory, ResearchCategoryAdmin)
admin.site.register(Research, ResearchAdmin)
