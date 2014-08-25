from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateField(null=True, blank=True)
    purchase_url = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='books')

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return self.title
