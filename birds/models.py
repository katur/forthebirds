import urllib

from django.core.urlresolvers import reverse
from django.db import models

from forthebirds.settings import MARKDOWN_PROMPT
from utils.http import http_response_url


class TaxonomicLevel(models.Model):
    name = models.CharField(max_length=20)
    depth = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name


class TaxonomicGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    common_name = models.CharField(max_length=50, blank=True)
    level = models.ForeignKey(TaxonomicLevel)
    parent = models.ForeignKey('self', null=True, blank=True)
    relative_position = models.PositiveSmallIntegerField(null=True,
                                                         blank=True)

    class Meta:
        ordering = ['level__depth', 'relative_position']

    def __unicode__(self):
        return self.common_name if self.common_name else self.name


class Species(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    # change to unique later
    ebird_id = models.CharField(max_length=10, blank=True)

    # delete later
    absolute_position = models.PositiveSmallIntegerField(
        'Taxonomic position', null=True, blank=True)

    # change to unique later
    taxon_order = models.DecimalField(
        max_digits=20, decimal_places=10, null=True, blank=True)

    # update these in place
    scientific_name = models.CharField(max_length=50, unique=True)
    common_name = models.CharField(max_length=50)

    # more new fields
    order = models.CharField(max_length=50, blank=True)
    family = models.CharField(max_length=50, blank=True)
    family_common = models.CharField(max_length=50, blank=True)
    en_IOC = models.CharField(max_length=50, blank=True)
    report_as = models.CharField(max_length=50, blank=True)

    # need to update this later, per any common_name updates
    slug = models.SlugField(max_length=50, unique=True)

    # these should not change
    is_visible = models.BooleanField('Visible on website', default=False)
    has_abc_bird_of_the_week_url = models.BooleanField(default=False)
    has_cornell_all_about_birds_url = models.BooleanField(default=False)
    blurb = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)
    main_photo_url = models.URLField(blank=True)
    main_sound_recording = models.ForeignKey(
        'creations.SoundRecording', null=True, blank=True,
        related_name='species_with_main_recording')

    # all these will be deleted later
    french_name = models.CharField(max_length=50)
    parent = models.ForeignKey(TaxonomicGroup)
    nacc_is_accidental = models.NullBooleanField()
    nacc_is_hawaiian = models.NullBooleanField()
    nacc_is_introduced = models.NullBooleanField()
    nacc_is_nonbreeding = models.NullBooleanField()
    nacc_is_extinct = models.NullBooleanField()
    nacc_is_misplaced = models.NullBooleanField()
    nacc_annotation = models.TextField(blank=True)

    class Meta:
        ordering = ['absolute_position']
        verbose_name_plural = 'bird species'

    def __unicode__(self):
        return self.common_name + ' (' + self.scientific_name + ')'

    def get_absolute_url(self):
        return reverse('bird_url', args=[self.slug])

    def get_ancestors(self):
        ancestors = []
        parent = self.parent

        while parent:
            ancestors.append(parent)
            parent = parent.parent

        return ancestors

    def get_ancestor(self, ancestor_level_name):
        for ancestor in self.get_ancestors():
            if ancestor.level.name == ancestor_level_name:
                return ancestor
        return None

    def get_order(self):
        return self.get_ancestor('order')

    def get_family(self):
        return self.get_ancestor('family')

    def get_subfamily(self):
        return self.get_ancestor('subfamily')

    def get_genus(self):
        return self.get_ancestor('genus')

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

    def get_flickr_search_url(self):
        url = 'https://www.flickr.com/search?'
        get_params = {
            'user_id': '48014585@N00',
            'sort': 'date-taken-desc',
            'text': self.common_name,
        }
        return url + urllib.urlencode(get_params)

    def get_nacc_statuses(self):
        statuses = []
        if self.nacc_is_accidental:
            statuses.append('Accidental')
        if self.nacc_is_hawaiian:
            statuses.append('Hawaiian')
        if self.nacc_is_introduced:
            statuses.append('Introduced')
        if self.nacc_is_nonbreeding:
            statuses.append('Non-breeding')
        if self.nacc_is_extinct:
            statuses.append('Extinct')
        if self.nacc_is_misplaced:
            statuses.append('Misplaced')
        return statuses


class MinnesotaSpecies(models.Model):
    species = models.OneToOneField(Species, primary_key=True)
    include_in_book = models.NullBooleanField(default=None)
    mou_status = models.CharField('MOU status', max_length=50, blank=True)
    mou_breeding_status = models.NullBooleanField('MOU breeding status',
                                                  default=None)
    mou_annotation = models.CharField('MOU annotation', max_length=500,
                                      blank=True)

    class Meta:
        ordering = ['species__absolute_position']
        verbose_name_plural = 'Minnesota species'

    def __unicode__(self):
        return str(self.species)
