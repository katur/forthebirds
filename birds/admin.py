from django import forms
from django.contrib import admin

from birds.models import Species
from creations.models import SoundRecording
from utils.admin import null_filter, empty_filter


EBIRD_FIELDS = (
    'common_name',
    'slug',
    'ebird_id',
    'taxon_order',
    'scientific_name',
    'family',
    'family_common',
    'order',
)


class SpeciesAdminForm(forms.ModelForm):

    class Meta:
        model = Species
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SpeciesAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            recordings = SoundRecording.objects.filter(species=self.instance)
            self.fields['main_sound_recording'].queryset = recordings


class HasCreationsFilter(admin.SimpleListFilter):
    """
    Admin list filter to filter for whether a bird has creations.
    """

    parameter_name = 'has_creations'
    title = 'has_creations'

    def lookups(self, request, model_admin):
        return (('0', 'No creations',), ('1', 'Has creations',),)

    def queryset(self, request, queryset):
        if self.value() not in ('0', '1'):
            return queryset

        filtered_pks = set()

        queryset = queryset.prefetch_related('creation_set').all()

        for bird in queryset:
            if self.value() == '0' and not bird.get_number_of_creations():
                filtered_pks.add(bird.pk)
            elif self.value() == '1' and bird.get_number_of_creations():
                filtered_pks.add(bird.pk)

        return Species.objects.filter(pk__in=filtered_pks)


class SpeciesAdmin(admin.ModelAdmin):

    form = SpeciesAdminForm

    list_display = (
        'common_name',
        'taxon_order',
        'is_visible',
        'has_blurb',
        'has_photo',
        'has_sound',
        'get_number_of_creations',
    )

    list_filter = (
        'is_visible',
        empty_filter('blurb'),
        empty_filter('main_photo_url'),
        null_filter('main_sound_recording'),
        HasCreationsFilter,
    )

    search_fields = (
        'scientific_name',
        'common_name',
    )

    readonly_fields = EBIRD_FIELDS

    fieldsets = (
        (None, {'fields': (
            'is_visible',
            'main_photo_url',
            'main_sound_recording',
            'blurb',
        )}),
        ('From eBird database', {'fields': EBIRD_FIELDS}),
    )


admin.site.register(Species, SpeciesAdmin)
