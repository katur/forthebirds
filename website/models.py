from django.contrib.auth.models import User
from django.db import models

from forthebirds.settings import MARKDOWN_PROMPT


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    about = models.TextField('Text for About page',
                             help_text=MARKDOWN_PROMPT, blank=True)
    primary_photo = models.FileField(null=True, blank=True,
                                     upload_to='photos_of_laura')

    def __unicode__(self):
        return self.user.get_full_name()
