from django import forms
from django.contrib import admin

from birds.models import Species, TaxonomicGroup
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

    list_display = ('common_name', 'slug', 'scientific_name',
                    'main_photo_url', 'absolute_position', 'is_visible',)

    list_filter = ('is_visible',)

    search_fields = ('scientific_name', 'common_name',)

    aou_fields = ('common_name', 'slug', 'scientific_name',
                  'parent', 'id', 'absolute_position',)

    readonly_fields = aou_fields

    fieldsets = (
        (None, {
            'fields': ('is_visible', 'main_photo_url',
                       'main_sound_recording', 'blurb',),
        }),
        ('From AOU checklist', {
            'fields': aou_fields,
        }),
    )


class TaxonomicGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'common_name', 'level', 'parent',
                    'relative_position',)

    list_filter = ('level',)

    search_fields = ('name', 'common_name',)

    aou_fields = ('name', 'level', 'parent', 'relative_position')

    readonly_fields = aou_fields

    fieldsets = (
        (None, {
            'fields': ('common_name',),
        }),
        ('From AOU checklist', {
            'fields': aou_fields,
        }),
    )


admin.site.register(Species, SpeciesAdmin)
admin.site.register(TaxonomicGroup, TaxonomicGroupAdmin)
