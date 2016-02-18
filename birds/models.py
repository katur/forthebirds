import urllib

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from utils.http import http_response_url


class Species(models.Model):
    """
    A bird species.
    """

    ebird_id = models.CharField(max_length=10, unique=True)
    taxon_order = models.DecimalField(
        max_digits=12, decimal_places=6, unique=True)
    common_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    # This is not used in project yet, but is another common name provided
    # by eBird
    en_IOC = models.CharField(max_length=75, unique=True)

    scientific_name = models.CharField(max_length=50, unique=True)
    family = models.CharField(max_length=50)
    family_common = models.CharField(max_length=50)
    order = models.CharField(max_length=50)

    is_visible = models.BooleanField('Visible on website', default=False)
    has_abc_bird_of_the_week_url = models.BooleanField(default=False)
    has_cornell_all_about_birds_url = models.BooleanField(default=False)
    has_wikipedia_url = models.BooleanField(default=False)

    blurb = models.TextField(blank=True, help_text=settings.MARKDOWN_PROMPT)
    main_photo_url = models.URLField(blank=True)
    main_sound_recording = models.ForeignKey(
        'creations.SoundRecording', null=True, blank=True,
        related_name='species_with_main_recording')

    class Meta:
        ordering = ['taxon_order']
        verbose_name_plural = 'bird species'

    def __unicode__(self):
        return self.common_name + ' (' + self.scientific_name + ')'

    def get_absolute_url(self):
        return reverse('bird_url', args=[self.slug])

    def get_flickr_search_url(self):
        url = 'https://www.flickr.com/search?'
        get_params = {
            'user_id': '48014585@N00',
            'sort': 'date-taken-desc',
            'text': self.common_name.encode('utf-8'),
        }
        return url + urllib.urlencode(get_params)

    def get_wikipedia_url(self):
        url_name = self.common_name.replace(' ', '_')
        url_name = urllib.quote_plus(url_name)
        return 'https://en.wikipedia.org/wiki/{}'.format(url_name)

    def get_resolved_wikipedia_url(self):
        return http_response_url(self.get_wikipedia_url())

    def get_abc_bird_of_the_week_url(self):
        url_name = self.common_name.replace(' ', '-')
        url_name = url_name.replace("'", '')
        return 'http://abcbirds.org/bird/{}/'.format(url_name)

    def get_resolved_abc_bird_of_the_week_url(self):
        return http_response_url(self.get_abc_bird_of_the_week_url())

    def get_cornell_all_about_birds_url(self):
        url_name = self.common_name.replace(' ', '_')
        url_name = url_name.replace("'", '')
        return 'http://www.allaboutbirds.org/guide/{}'.format(url_name)

    def get_resolved_cornell_all_about_birds_url(self):
        url = http_response_url(self.get_cornell_all_about_birds_url())
        if url and 'search' in url:
            url = None
        return url
