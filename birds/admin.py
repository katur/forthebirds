from django.contrib import admin

from birds.models import (Species, TaxonomicGroup)


class SpeciesAdmin(admin.ModelAdmin):
    list_display = (
        'common_name',
        'name',
        'bird_of_the_week_name',
        'main_photo_url',
        'absolute_position',
        'is_hidden',
    )

    list_filter = (
        'is_hidden',
        'nacc_is_accidental',
        'nacc_is_hawaiian',
        'nacc_is_introduced',
        'nacc_is_nonbreeding',
        'nacc_is_extinct',
        'nacc_is_misplaced',
    )

    list_editable = (
        'is_hidden',
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
admin.site.register(TaxonomicGroup, TaxonomicGroupAdmin)
