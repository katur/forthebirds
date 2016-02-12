from django import forms
from django.contrib import admin

from birds.models import Species
from creations.models import SoundRecording


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

    list_display = ('common_name', 'is_visible', 'taxon_order',
                    'scientific_name', 'main_photo_url',)

    list_filter = ('is_visible',)

    search_fields = ('scientific_name', 'common_name',)

    ebird_fields = ('common_name', 'slug', 'ebird_id', 'taxon_order',
                    'scientific_name', 'family', 'family_common', 'order',)

    readonly_fields = ebird_fields

    fieldsets = (
        (None, {
            'fields': ('is_visible', 'main_photo_url',
                       'main_sound_recording', 'blurb',),
        }),
        ('From eBird database', {
            'fields': ebird_fields,
        }),
    )


admin.site.register(Species, SpeciesAdmin)
