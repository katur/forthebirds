import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail


def get_updated_filename(instance, filename):
    path = "images/{}_{}".format(uuid.uuid4(), filename)
    return path


class UploadedImage(models.Model):
    image = ImageField(upload_to=get_updated_filename)
    time_uploaded = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    attribution = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        x = self.title
        if self.attribution:
            x = '{} ({})'.format(x, self.attribution)
        return x

    def __str__(self):
        return unicode(self).encode('utf-8')

    def get_url(self):
        return self.image.url

    get_url.short_description = 'Path to fullsize image'

    def get_thumbnail_img_tag(self):
        thumbnail = get_thumbnail(self.image, '90')
        return u'<img src="{}" />'.format(thumbnail.url)

    # Allow get_thumbnail_img_tag to render in Admin
    get_thumbnail_img_tag.allow_tags = True
    get_thumbnail_img_tag.short_description = 'Preview'


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    blurb = models.TextField(help_text=settings.MARKDOWN_PROMPT, blank=True)
    bio = models.TextField(help_text=settings.MARKDOWN_PROMPT, blank=True)
    awards = models.TextField(help_text=settings.MARKDOWN_PROMPT, blank=True)
    main_photo = models.ForeignKey(
        UploadedImage, null=True, blank=True,
        related_name='main_uploaded_photo', on_delete=models.SET_NULL)
    publicity_photos = models.ManyToManyField(
        UploadedImage, related_name='uploaded_publicity_photos', blank=True)
    speaking_overview = models.TextField(
        help_text=settings.MARKDOWN_PROMPT, blank=True)
    speaking_keynotes = models.TextField(
        help_text=settings.MARKDOWN_PROMPT, blank=True)
    speaking_testimonials = models.TextField(
        help_text=settings.MARKDOWN_PROMPT, blank=True)

    def __unicode__(self):
        return self.user.get_full_name()

    def __str__(self):
        return unicode(self).encode('utf-8')

class PatreonThankYou(models.Model):
    text = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return unicode(self).encode('utf-8')
