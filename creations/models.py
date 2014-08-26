from django.db import models


class Creation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title


class Book(Creation):
    purchase_url = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='books')
    year_published = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-year_published']


class RadioProgram(Creation):
    original_air_date = models.DateField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='radio')
    supplemental_content_url = models.CharField(max_length=500, blank=True)
    transcript = models.TextField(blank=True)

    class Meta:
        ordering = ['-original_air_date']
