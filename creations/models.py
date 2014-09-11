from django.db import models

from taggit.managers import TaggableManager

from birds.models import Species


class Creation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    species = models.ManyToManyField(Species, blank=True)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title


class Book(Creation):
    purchase_url = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='books')
    publisher = models.CharField(max_length=100, blank=True)
    isbn_10 = models.CharField(max_length=20, blank=True)
    isbn_13 = models.CharField(max_length=20, blank=True)
    date_published = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date_published']


class RadioProgram(Creation):
    original_air_date = models.DateField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='radio')
    supplemental_content_url = models.CharField(max_length=500, blank=True)
    transcript = models.TextField(blank=True)

    class Meta:
        ordering = ['-original_air_date']
