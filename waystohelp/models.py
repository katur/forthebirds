from django.core.urlresolvers import reverse
from django.db import models

from forthebirds.settings import MARKDOWN_PROMPT


class WayToHelp(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'ways to help'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('waystohelp.views.way_to_help', args=[self.id])
