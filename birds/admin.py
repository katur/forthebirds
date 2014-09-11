from django.contrib import admin

from birds.models import (Species, MinnesotaSpecies, TaxonomicGroup)


def add_to_minnesota_species(modeladmin, request, queryset):
    for species in queryset:
        print species
        try:
            minnesota_species = MinnesotaSpecies.objects.get(
                species=species)
        except MinnesotaSpecies.DoesNotExist:
            minnesota_species = MinnesotaSpecies(species=species)
            minnesota_species.save()
add_to_minnesota_species.short_description = ('Add this bird to MN list if '
                                              'not already there')


class SpeciesAdmin(admin.ModelAdmin):
    list_display = (
        'common_name',
        'name',
        'bird_of_the_week_name',
        'main_photo_url',
        'absolute_position',
        'is_hidden',
        'is_in_minnesota_list',
    )

    def is_in_minnesota_list(self, obj):
        try:
            MinnesotaSpecies.objects.get(species=obj)
            return True
        except MinnesotaSpecies.DoesNotExist:
            return False
    is_in_minnesota_list.boolean = True

    list_filter = (
        'is_hidden',
        'nacc_is_accidental',
        'nacc_is_hawaiian',
        'nacc_is_introduced',
        'nacc_is_nonbreeding',
        'nacc_is_extinct',
        'nacc_is_misplaced',
    )

    search_fields = (
        'name',
        'common_name',
    )

    readonly_fields = ('common_name', 'name', 'french_name', 'parent',
                       'id', 'absolute_position',
                       'nacc_is_accidental',
                       'nacc_is_hawaiian', 'nacc_is_introduced',
                       'nacc_is_nonbreeding', 'nacc_is_extinct',
                       'nacc_is_misplaced', 'nacc_annotation')

    actions = [add_to_minnesota_species]


class MinnesotaSpeciesAdmin(admin.ModelAdmin):
    list_display = (
        'species',
        'include_in_book',
        'mou_status',
        'mou_breeding_status',
        'mou_annotation',
    )

    list_filter = (
        'include_in_book',
        'mou_status',
        'mou_breeding_status',
    )

    list_editable = (
        'mou_breeding_status',
        'mou_annotation',
    )

    search_fields = (
        'species__common_name',
        'species__name',
    )


class TaxonomicGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'common_name',
        'level',
        'parent',
        'relative_position',
    )

    list_editable = (
        'common_name',
    )

    list_filter = (
        'level',
    )

    search_fields = (
        'name',
        'common_name',
    )

    readonly_fields = ('name', 'level', 'parent', 'relative_position')


admin.site.register(Species, SpeciesAdmin)
admin.site.register(MinnesotaSpecies, MinnesotaSpeciesAdmin)
admin.site.register(TaxonomicGroup, TaxonomicGroupAdmin)
