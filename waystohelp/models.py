from django.conf import settings
from django.db import models
from django.urls import reverse

from website.models import UploadedImage


class WayToHelp(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, help_text=settings.MARKDOWN_PROMPT)
    background_image = models.ForeignKey(
        UploadedImage, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'ways to help'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('way_to_help_url', args=[self.id])
