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
