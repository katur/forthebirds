import binascii
import math
from mutagen.mp3 import MP3
import re

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager
from private_media.storages import PrivateMediaStorage

from forthebirds.settings import MARKDOWN_PROMPT, MEDIA_ROOT
from birds.models import Species
from website.models import UploadedImage
from utils.models import RealInstanceProvider


class Creation(models.Model, RealInstanceProvider):
    """Superclass for one of Laura's creations."""
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)
    species = models.ManyToManyField(Species, blank=True)
    tags = TaggableManager(blank=True)
    is_public = True
    is_image = False

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return None

    def get_class_display_name(self):
        if self.is_research():
            ancestors = list(reversed(self.get_ancestors()))
            ancestors.append(self.title)
            return u'\N{RIGHTWARDS ARROW}'.join(
                (unicode(a) for a in ancestors))

        else:
            class_name = self.__class__.__name__
            words = re.findall('[A-Z][^A-Z]*', class_name)
            return ' '.join(words)

    def get_display_date(self):
        if hasattr(self, 'date_published'):
            return self.date_published
        else:
            return None

    def is_research(self):
        class_name = self.__class__.__name__
        return class_name.lower() == 'research'

    def has_tags(self):
        return len(self.species.all()) or len(self.tags.names())


class Article(Creation):
    """An article written by Laura."""
    published_by = models.CharField(max_length=100, blank=True)
    date_published = models.DateField(null=True, blank=True)
    url = models.URLField(blank=True)
    file = models.FileField(null=True, blank=True, upload_to='articles')
    text = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return 'Article: ' + self.title

    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return reverse('article_url',
                           args=[self.id, slugify(self.title)])


class BlogPost(Creation):
    """A blog post, written on another domain, written by Laura."""
    url = models.URLField()

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return 'Blog Post: ' + self.title

    def get_absolute_url(self):
        return self.url


class Book(Creation):
    """A book written by Laura."""
    slug = models.SlugField(max_length=120, unique=True)
    published_by = models.CharField(max_length=100, blank=True)
    date_published = models.DateField(null=True, blank=True)
    purchase_url = models.URLField(blank=True)
    cover_photo = models.ForeignKey(UploadedImage, null=True, blank=True,
                                    on_delete=models.SET_NULL)
    isbn_10 = models.CharField('ISBN 10', max_length=20, blank=True)
    isbn_13 = models.CharField('ISBN 13', max_length=20, blank=True)

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return 'Book: ' + self.title

    def get_absolute_url(self):
        return reverse('book_url', args=[self.slug])


class ExternalProject(Creation):
    """One of Laura's projects hosted on an external domain."""
    url = models.URLField()
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'title']

    def __unicode__(self):
        return 'External Project: ' + self.title

    def get_absolute_url(self):
        return self.url


class RadioProgram(Creation):
    """A For the Birds radio program."""
    file = models.FileField(upload_to='radio')
    air_date = models.DateField()

    # Duration in seconds
    duration = models.PositiveIntegerField(blank=True, null=True)

    supplemental_content_url = models.URLField(blank=True)
    transcript = models.TextField(blank=True,
                                  help_text=MARKDOWN_PROMPT)

    class Meta:
        ordering = ['-air_date']

    def __unicode__(self):
        return 'Radio Program: ' + self.title

    def get_absolute_url(self):
        return reverse('radio_program_url',
                       args=[self.id, slugify(self.title)])

    def get_display_date(self):
        return self.air_date

    def get_reruns(self):
        return self.radioprogramrerun_set

    def get_artwork(self):
        """
        Get artwork embedded in this program's mp3 file.
        Returns the artwork as a line of ASCII characters in base64 coding.
        """
        try:
            program_path = '{}/{}'.format(MEDIA_ROOT, self.file.name)
            artwork = MP3(program_path).tags['APIC:'].data
            base64 = binascii.b2a_base64(artwork)
            return base64

        except Exception:
            return None

    def calculate_duration(self):
        """
        Caculate this program's duration by reading the mp3 file.
        """
        try:
            program_path = '{}/{}'.format(MEDIA_ROOT, self.file.name)
            return int(math.ceil(MP3(program_path).info.length))

        except Exception:
            return None

    def get_minutes_and_seconds(self):
        """
        Get program duration as tuple (minutes, seconds).

        Minutes and seconds are both integers.
        """
        if self.duration:
            minutes = self.duration // 60
            seconds = self.duration % 60
        else:
            minutes = None
            seconds = None

        return (minutes, seconds)

    def get_itunes_duration(self):
        """
        Get program duration as string in format min:sec
        """
        if self.duration:
            minutes, seconds = self.get_minutes_and_seconds()
            return '{}:{:02d}'.format(minutes, seconds)
        else:
            return '0:00'

    def get_printable_duration(self):
        """
        Get program duration as string in format min'sec"
        """
        if self.duration:
            minutes, seconds = self.get_minutes_and_seconds()
            return u'{0}{1}{2:02d}{3}'.format(
                minutes, u'\N{PRIME}', seconds, u'\N{DOUBLE PRIME}')
        else:
            return 'N/A'


@receiver(post_save, sender=RadioProgram)
def add_radio_program_duration(sender, instance, **kwargs):
    """
    Signal handler to set the program duration after it is saved.

    Using a post_save signal because the file is not saved to its
    eventual disk location until the end of the save method,
    and the MP3 library takes a disk location arg for the file.

    Need to disconnect this signal handler during function execution,
    so that the post_save handler is not sent recursively.
    """
    if not instance.duration:
        post_save.disconnect(add_radio_program_duration, sender=sender)
        instance.duration = instance.calculate_duration()
        instance.save()
        post_save.connect(add_radio_program_duration, sender=sender)


class RadioProgramRerun(models.Model):
    """A rerun airing of a RadioProgram."""
    program = models.ForeignKey(RadioProgram)
    air_date = models.DateField()

    class Meta:
        ordering = ['-air_date']

    def __unicode__(self):
        return '{} aired {}'.format(self.program, self.air_date)


class ResearchCategory(models.Model):
    """A category of Laura's private research."""
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'research categories'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('research_category_url', args=[self.id])

    def get_ancestors(self):
        ancestors = []
        parent = self.parent
        while parent:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors


class Research(Creation):
    """A typically-private research item of Laura's."""
    category = models.ForeignKey(ResearchCategory)
    is_public = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    attribution = models.CharField(max_length=200, blank=True,
                                   help_text=MARKDOWN_PROMPT)
    url = models.URLField(blank=True)
    file = models.FileField(null=True, blank=True, upload_to='research')
    text = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Research'

    def __unicode__(self):
        return 'Research: ' + self.title

    def get_absolute_url(self):
        return reverse('research_item_url', args=[self.id])

    def get_ancestors(self):
        ancestors = [self.category]
        ancestors.extend(self.category.get_ancestors())
        return ancestors


class SpeakingProgram(Creation):
    """A public speaking program."""
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return 'Speaking Program: ' + self.title

    def get_absolute_url(self):
        return reverse('speaking_program_url', args=[self.slug])


class SpeakingProgramFile(models.Model):
    """A file (typically a Powerpoint) to use during a SpeakingProgram."""
    program = models.ForeignKey(SpeakingProgram)
    title = models.CharField(max_length=120)
    file = models.FileField(upload_to='speaking',
                            storage=PrivateMediaStorage())
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return 'Speaking Presentation File: ' + self.title

    def get_absolute_url(self):
        return self.file.url


class WebPage(Creation):
    """A static web page of Laura's to be displayed within this website."""
    slug = models.SlugField(max_length=120, unique=True)
    date_published = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)
    display_title = models.BooleanField(default=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'title']

    def __unicode__(self):
        return 'Web Page: ' + self.title

    def get_absolute_url(self):
        return reverse('webpage_url', args=[self.slug])


class ABAFieldGuideImage(Creation):
    image = models.ImageField(null=True, blank=True, upload_to='abafieldguide')
    is_public = False
    is_image = True

    class Meta:
        ordering = ['title']
        verbose_name = 'ABA Field Guide Images'

    def __unicode__(self):
        return 'ABA Field Guide Image ' + self.title

    def get_absolute_url(self):
        return self.image.url
