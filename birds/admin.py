from django.contrib import admin

from birds.models import Species, MinnesotaSpecies, TaxonomicGroup


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
    list_display = ('common_name', 'name', 'bird_of_the_week_name',
                    'main_photo_url', 'absolute_position', 'is_visible',
                    'is_in_minnesota_list',)

    list_filter = ('is_visible', 'nacc_is_accidental', 'nacc_is_hawaiian',
                   'nacc_is_introduced', 'nacc_is_nonbreeding',
                   'nacc_is_extinct', 'nacc_is_misplaced',)

    search_fields = ('name', 'common_name',)

    actions = [add_to_minnesota_species]

    aou_fields = ('common_name', 'name', 'parent',
                  'id', 'absolute_position',
                  'french_name', 'nacc_is_accidental',
                  'nacc_is_hawaiian', 'nacc_is_introduced',
                  'nacc_is_nonbreeding', 'nacc_is_extinct',
                  'nacc_is_misplaced', 'nacc_annotation')

    readonly_fields = aou_fields

    fieldsets = (
        (None, {
            'fields': ('is_visible', 'main_photo_url',
                       'blurb', 'bird_of_the_week_name',),
        }),
        ('From AOU checklist', {
            'fields': aou_fields,
        }),
    )

    def is_in_minnesota_list(self, obj):
        try:
            MinnesotaSpecies.objects.get(species=obj)
            return True
        except MinnesotaSpecies.DoesNotExist:
            return False
    is_in_minnesota_list.boolean = True


class MinnesotaSpeciesAdmin(admin.ModelAdmin):
    list_display = ('species', 'include_in_book', 'mou_status',
                    'mou_breeding_status', 'mou_annotation',)

    list_filter = ('include_in_book', 'mou_status', 'mou_breeding_status',)

    search_fields = ('species__common_name', 'species__name',)

    mou_fields = ('mou_status', 'mou_breeding_status', 'mou_annotation',)

    readonly_fields = ('species',)

    fieldsets = (
        (None, {
            'fields': ('species', 'include_in_book', 'range_in_minnesota',
                       'miscellaneous_notes',),
        }),
        ('From MOU checklist', {
            'fields': mou_fields,
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
admin.site.register(MinnesotaSpecies, MinnesotaSpeciesAdmin)
admin.site.register(TaxonomicGroup, TaxonomicGroupAdmin)
