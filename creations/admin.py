from django import forms
from django.contrib import admin

from creations.models import (
    Article, BlogPost, Book, ExternalProject,
    RadioProgram, RadioProgramRerun, RadioProgramMissedDate,
    ResearchCategory, Research, SoundRecording,
    SpeakingProgram, SpeakingProgramFile, WebPage)
from utils.admin import empty_filter


BASIC_FIELDSET = (None, {'fields': (
    'title',
    'description',
    'is_favorite',
)})

BASIC_FIELDSET_WITH_SLUG = (None, {'fields': (
    'title',
    'slug',
    'description',
    'is_favorite',
)})

TAGGING_FIELDSET = ('Tagging', {'fields': (
    'species',
    'tags',
)})


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'date_published',
        'published_by'
    )

    filter_horizontal = (
        'species',
    )

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields': (
            'published_by',
            'date_published',
            'url',
            'file',
            'text',
        )}),
        TAGGING_FIELDSET,
    )


class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'url',
    )

    filter_horizontal = (
        'species',
    )

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields': (
            'url',
        )}),
        TAGGING_FIELDSET,
    )


class BookAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'date_published',
    )

    filter_horizontal = (
        'species',
    )

    prepopulated_fields = {
        'slug': ('title',),
    }

    fieldsets = (
        BASIC_FIELDSET_WITH_SLUG,
        ('Details', {'fields': (
            'published_by',
            'date_published',
            'isbn_10',
            'isbn_13',
            'purchase_url',
            'cover_photo',
        )}),
        TAGGING_FIELDSET,
    )


class ExternalProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'url',
        'display_order',
    )

    list_editable = (
        'display_order',
    )

    filter_horizontal = (
        'species',
    )

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields': (
            'url',
        )}),
        TAGGING_FIELDSET,
    )


class AirYearListFilter(admin.SimpleListFilter):
    """
    Admin list filter to filter by air_date year.
    """

    title = 'air date year'
    parameter_name = 'air_date'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        date_list = qs.dates('air_date', 'year')
        return [(d.year, d.year) for d in reversed(date_list)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(air_date__year=self.value())
        else:
            return queryset


class RadioProgramRerunInline(admin.TabularInline):

    model = RadioProgramRerun


class RadioProgramAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'air_date',
        'date_is_estimate',
        'file',
        'has_blog_url',
        'has_transcript',
        'get_number_of_reruns',
    )

    list_filter = (
        'date_is_estimate',
        empty_filter('file'),
        empty_filter('blog_url'),
        empty_filter('transcript'),
        AirYearListFilter,
    )

    search_fields = (
        'title',
    )

    filter_horizontal = (
        'species',
    )

    inlines = [RadioProgramRerunInline]

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields': (
            'air_date',
            'date_is_estimate',
            'file',
            'blog_url',
            'transcript',
        )}),
        TAGGING_FIELDSET,
    )


class RadioProgramMissedDateAdmin(admin.ModelAdmin):

    list_display = (
        'air_date',
        'text',
    )

    search_fields = (
        'text',
    )


class ResearchCategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )


class ResearchAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'attribution',
        'date',
        'url',
    )

    list_filter = (
        'category',
    )

    search_fields = (
        'title',
        'attribution',
        'description',
    )

    filter_horizontal = (
        'species',
    )

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields': (
            'category',
            'is_public',
            'date',
            'attribution',
            'url',
            'file',
            'text',
        )}),
        TAGGING_FIELDSET,
    )


class SoundRecordingAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'date_recorded',
        'location',
        'duration',
        'file',
    )

    search_fields = (
        'title',
        'location',
        'description',
    )

    filter_horizontal = (
        'species',
    )

    fieldsets = (
        BASIC_FIELDSET,
        ('Details', {'fields': (
            'file',
            'date_recorded',
            'location',
        )}),
        TAGGING_FIELDSET,
    )


class SpeakingProgramFileInline(admin.TabularInline):

    model = SpeakingProgramFile


class SpeakingProgramAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
    )

    filter_horizontal = (
        'species',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    inlines = [SpeakingProgramFileInline]

    fieldsets = (
        BASIC_FIELDSET_WITH_SLUG,
        TAGGING_FIELDSET,
    )


class WebPageAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(WebPageAdminForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget = admin.widgets.AdminTextareaWidget(
            attrs={'cols': 100, 'rows': 100, 'style': 'font-size: 14px;'})


class WebPageAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'display_order',
    )

    list_editable = (
        'display_order',
    )

    filter_horizontal = (
        'species',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    fieldsets = (
        BASIC_FIELDSET_WITH_SLUG,
        ('Details', {'fields': (
            'is_public',
            'display_title',
            'date_published',
            'content',
        )}),
        TAGGING_FIELDSET,
    )

    form = WebPageAdminForm


admin.site.register(Article, ArticleAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(ExternalProject, ExternalProjectAdmin)
admin.site.register(RadioProgram, RadioProgramAdmin)
admin.site.register(RadioProgramMissedDate, RadioProgramMissedDateAdmin)
admin.site.register(ResearchCategory, ResearchCategoryAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(SoundRecording, SoundRecordingAdmin)
admin.site.register(SpeakingProgram, SpeakingProgramAdmin)
admin.site.register(WebPage, WebPageAdmin)
