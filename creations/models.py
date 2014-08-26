from django.db import models


class Creation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_published = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return self.title


class Book(Creation):
    purchase_url = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='books')


class RadioProgram(Creation):
    transcript = models.TextField(blank=True)
    file = models.FileField(null=True, blank=True, upload_to='radio')
