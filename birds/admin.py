from django.contrib import admin

from birds.models import (Species, TaxonomicGroup)


class SpeciesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'common_name',
        'absolute_position',
        'parent',
    )

    list_filter = (
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


admin.site.register(Species, SpeciesAdmin)
admin.site.register(TaxonomicGroup, TaxonomicGroupAdmin)
