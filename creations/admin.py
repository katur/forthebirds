from django.contrib import admin

from creations.models import (RadioProgram, RadioProgramRerun,
                              Book, Article, BlogPost,
                              WebPage, ExternalProject,
                              SpeakingProgram, SpeakingProgramFile,
                              Research, ResearchCategory)


BASIC_FIELDSET = (None, {'fields': ('title', 'description',)})
BASIC_FIELDSET_WITH_SLUG = (None, {'fields':
    ('title', 'slug', 'description',)})
TAGGING_FIELDSET = ('Tagging', {'fields': ('species', 'tags',)})


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'published_by')
    filter_horizontal = ('species',)

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields':
            ('published_by', 'date_published', 'url', 'file', 'text'),
        }),
        TAGGING_FIELDSET,
    )


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    filter_horizontal = ('species',)

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields': ('url',),}),
        TAGGING_FIELDSET,
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published',)
    filter_horizontal = ('species',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        BASIC_FIELDSET_WITH_SLUG,
        ('Details', {'fields':
            ('publisher', 'isbn_10', 'isbn_13', 'date_published',
             'purchase_url', 'cover_photo'),
        }),
        TAGGING_FIELDSET,
    )


class RadioProgramRerunInline(admin.TabularInline):
    model = RadioProgramRerun


class RadioProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'air_date', 'file',)
    list_filter = ('air_date',)
    search_fields = ('title',)
    filter_horizontal = ('species',)

    inlines = [RadioProgramRerunInline]

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields':
            ('air_date', 'file', 'supplemental_content_url',
             'transcript',),
        }),
        TAGGING_FIELDSET,
    )


class SpeakingProgramFileInline(admin.TabularInline):
    model = SpeakingProgramFile


class SpeakingProgramAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('species',)
    prepopulated_fields = {'slug': ('title',)}

    inlines = [SpeakingProgramFileInline]

    fieldsets = (
        BASIC_FIELDSET_WITH_SLUG,
        TAGGING_FIELDSET,
    )


class WebPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('species',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        BASIC_FIELDSET_WITH_SLUG,
        ('Details', {'fields':
            ('date_published', 'content',),
        }),
        TAGGING_FIELDSET,
    )


class ExternalProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    filter_horizontal = ('species',)

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields': ('url',),}),
        TAGGING_FIELDSET,
    )


class ResearchCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'attribution', 'date', 'url',)
    list_filter = ('category',)
    search_fields = ('title', 'attribution', 'description',)
    filter_horizontal = ('species',)

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields':
            ('category', 'is_public', 'date', 'attribution',
             'url', 'file', 'text'),
        }),
        TAGGING_FIELDSET,
    )


admin.site.register(RadioProgram, RadioProgramAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(SpeakingProgram, SpeakingProgramAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(ExternalProject, ExternalProjectAdmin)
admin.site.register(ResearchCategory, ResearchCategoryAdmin)
admin.site.register(Research, ResearchAdmin)
