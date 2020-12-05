from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from sorl.thumbnail.admin import AdminImageMixin

from website.models import UserProfile, UploadedImage, PatreonThankYou


class UserProfileInline(admin.StackedInline):

    model = UserProfile
    can_delete = False
    verbose_name_plural = 'about'

    filter_horizontal = (
        'publicity_photos',
    )


class MyUserAdmin(UserAdmin):
    """
    Extends Django's UserAdmin class to include UserProfile inline
    """

    inlines = (UserProfileInline,)


class UploadedImageAdmin(AdminImageMixin, admin.ModelAdmin):

    list_display = ('get_thumbnail_img_tag', 'title', 'attribution',
                    'get_url')
    readonly_fields = ('get_url',)
    search_fields = ('title', 'attribution',)


class PatreonThankYouAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(UploadedImage, UploadedImageAdmin)
admin.site.register(PatreonThankYou, PatreonThankYouAdmin)
