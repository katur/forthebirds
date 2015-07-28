import uuid

from django.contrib.auth.models import User
from django.db import models

from forthebirds.settings import MARKDOWN_PROMPT


def get_updated_filename(instance, filename):
    path = "images/{}_{}".format(uuid.uuid4(), filename)
    return path


class UploadedImage(models.Model):
    time_uploaded = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=get_updated_filename)

    def image_tag(self):
        return u'<img style="max-width: 500px" src="%s" />' % self.image.url

    def url(self):
        return self.image.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.title

    def __str__(self):
        return unicode(self).encode('utf-8')


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    blurb = models.TextField(help_text=MARKDOWN_PROMPT, blank=True)
    bio = models.TextField(help_text=MARKDOWN_PROMPT, blank=True)
    awards = models.TextField(help_text=MARKDOWN_PROMPT, blank=True)
    main_photo = models.ForeignKey(UploadedImage, null=True, blank=True,
                                   related_name='main_uploaded_photo')
    publicity_photos = models.ManyToManyField(
        UploadedImage, related_name='uploaded_publicity_photos', blank=True)
    speaking_overview = models.TextField(help_text=MARKDOWN_PROMPT, blank=True)
    speaking_keynotes = models.TextField(help_text=MARKDOWN_PROMPT, blank=True)
    speaking_testimonials = models.TextField(help_text=MARKDOWN_PROMPT,
                                             blank=True)

    def __unicode__(self):
        return self.user.get_full_name()

    def __str__(self):
        return unicode(self).encode('utf-8')
