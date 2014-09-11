from django.contrib import admin

from waystohelp.models import WayToHelp


class WayToHelpAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

admin.site.register(WayToHelp, WayToHelpAdmin)
