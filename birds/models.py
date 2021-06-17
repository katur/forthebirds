import urllib

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from birds.helpers.flickr import search_flickr
from forthebirds.localsettings import FLICKR_USER_ID
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

    is_visible = models.BooleanField(default=False)

    has_abc_bird_of_the_week_url = models.BooleanField(default=False)
    has_cornell_all_about_birds_url = models.BooleanField(default=False)
    has_mn_bird_atlas_url = models.BooleanField(default=False)
    has_wikipedia_url = models.BooleanField(default=False)

    blurb = models.TextField(blank=True, help_text=settings.MARKDOWN_PROMPT)
    main_photo_url = models.URLField(blank=True)
    main_sound_recording = models.ForeignKey(
        'creations.SoundRecording', models.SET_NULL,
        null=True, blank=True,
        related_name='species_with_main_recording')

    class Meta:
        ordering = ['taxon_order']
        verbose_name_plural = 'bird species'

    def __str__(self):
        return self.common_name + ' (' + self.scientific_name + ')'

    def get_absolute_url(self):
        return reverse('bird_url', args=[self.slug])

    def has_blurb(self):
        return self.blurb != ''
    has_blurb.boolean = True

    def has_photo(self):
        return self.main_photo_url != ''
    has_photo.boolean = True

    def has_sound(self):
        return self.main_sound_recording is not None
    has_sound.boolean = True

    def get_number_of_creations(self):
        return len(self.creation_set.all())
    get_number_of_creations.short_description = 'Num creations'

    def get_number_of_radio_programs(self):
        programs = [c for c in self.creation_set.all() if c.is_radio_program()]
        return len(programs)
    get_number_of_radio_programs.short_description = 'Num programs'

    def get_flickr_search_url(self):
        url = 'https://www.flickr.com/search?'
        get_params = {
            'user_id': FLICKR_USER_ID,
            'sort': 'date-taken-desc',
            'text': self.common_name.encode('utf-8'),
        }
        return url + urllib.parse.urlencode(get_params)

    def get_abc_bird_of_the_week_url(self):
        url_name = self.common_name.replace(' ', '-').replace("'", '')
        return 'https://abcbirds.org/bird/{}'.format(url_name)

    def get_cornell_all_about_birds_url(self):
        url_name = self.common_name.replace(' ', '_').replace("'", '')
        return 'https://www.allaboutbirds.org/guide/{}'.format(url_name)

    def get_mn_bird_atlas_url(self):
        url_name = self.common_name.replace(' ', '-').replace("'", '')
        return 'https://mnbirdatlas.org/species/{}'.format(url_name)

    def get_wikipedia_url(self):
        url_name = urllib.parse.quote_plus(self.common_name.replace(' ', '_'))
        return 'https://en.wikipedia.org/wiki/{}'.format(url_name)

    def get_resolved_abc_bird_of_the_week_url(self):
        return http_response_url(self.get_abc_bird_of_the_week_url())

    def get_resolved_cornell_all_about_birds_url(self):
        url = http_response_url(self.get_cornell_all_about_birds_url())
        if url and 'search' in url:
            url = None
        return url

    def get_resolved_mn_bird_atlas_url(self):
        return http_response_url(self.get_mn_bird_atlas_url())

    def get_resolved_wikipedia_url(self):
        return http_response_url(self.get_wikipedia_url())

    def get_lauras_flickr_photos(self):
        """
        Get Laura's "additional Flickr photos" for this bird.

        First attempts to find photos with the tag "website" in addition
        to this bird's common_name. This is Laura's tag to select
        particular favorites to show on the website. Finds up to 100
        of these images.

        If no results are found with "website", then it returns up to 12
        photos tagged with common_name only.
        """
        common_name = self.common_name
        photos = search_flickr([common_name, 'website'], per_page=100)

        if photos['photos']['total'] == 0:
            photos = search_flickr([common_name], per_page=12)

        return photos
