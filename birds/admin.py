from django import forms
from django.contrib import admin

from birds.models import Species
from creations.models import SoundRecording


class NullListFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        return (('0', 'Not None', ), ('1', 'None', ),)

    def queryset(self, request, queryset):
        if self.value() in ('0', '1'):
            kwargs = {
                '{0}__isnull'.format(self.parameter_name): self.value() == '1'
            }
            return queryset.filter(**kwargs)
        return queryset


def null_filter(field, title_=None):
    class NullListFieldFilter(NullListFilter):
        parameter_name = field
        title = title_ or parameter_name
    return NullListFieldFilter


class EmptyListFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        return (('0', 'Not None',), ('1', 'None', ),)

    def queryset(self, request, queryset):
        kwargs = {'{}__exact'.format(self.parameter_name): ''}

        if self.value() == '1':
            return queryset.filter(**kwargs)
        elif self.value() == '0':
            return queryset.exclude(**kwargs)

        else:
            return queryset


def empty_filter(field, title_=None):
    class EmptyListFieldFilter(EmptyListFilter):
        parameter_name = field
        title = title_ or parameter_name
    return EmptyListFieldFilter


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

    list_display = ('common_name', 'taxon_order', 'is_visible',
                    'has_blurb', 'has_photo', 'has_sound',
                    'get_number_of_creations',)

    list_filter = (
        'is_visible',
        empty_filter('blurb'),
        empty_filter('main_photo_url'),
        null_filter('main_sound_recording'),
    )

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
