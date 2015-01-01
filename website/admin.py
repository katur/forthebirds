from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from website.models import UserProfile, UploadedImage


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'about'


class MyUserAdmin(UserAdmin):
    """
    Extends Django's UserAdmin class to include UserProfile inline
    """
    inlines = (UserProfileInline,)


class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    readonly_fields = ('url', 'image_tag',)


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(UploadedImage, UploadedImageAdmin)
