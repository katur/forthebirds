from django.db import models
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

from forthebirds.settings import MARKDOWN_PROMPT
from birds.models import Species
from utils.models import RealInstanceProvider


class Creation(models.Model, RealInstanceProvider):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   help_text=MARKDOWN_PROMPT)
    species = models.ManyToManyField(Species, blank=True)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return None


class Book(Creation):
    purchase_url = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='books')
    publisher = models.CharField(max_length=100, blank=True)
    isbn_10 = models.CharField('ISBN 10', max_length=20, blank=True)
    isbn_13 = models.CharField('ISBN 13', max_length=20, blank=True)
    date_published = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date_published']

    def get_absolute_url(self):
        return reverse('creations.views.books')

    def __unicode__(self):
        return 'Book: ' + self.title


class RadioProgram(Creation):
    original_air_date = models.DateField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='radio')
    supplemental_content_url = models.CharField(max_length=500, blank=True)
    transcript = models.TextField(blank=True,
                                  help_text=MARKDOWN_PROMPT)

    class Meta:
        ordering = ['-original_air_date']

    def get_absolute_url(self):
        return reverse('creations.views.radio')

    def __unicode__(self):
        return 'Radio Program: ' + self.title
