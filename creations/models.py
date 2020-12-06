import binascii
import math
from mutagen.mp3 import MP3
import re

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

from birds.models import Species
from website.models import UploadedImage
from utils.models import RealInstanceProvider


def get_artwork_from_file(obj):
    """
    Get artwork embedded in obj's mp3 file.
    Returns the artwork as a line of ASCII characters in base64 coding.
    """
    try:
        program_path = '{}/{}'.format(settings.MEDIA_ROOT, obj.file.name)
        artwork = MP3(program_path).tags['APIC:'].data
        return binascii.b2a_base64(artwork).decode('ascii')

    except Exception:
        return None


def get_duration_from_file(obj):
    """
    Get the duration in seconds of obj's mp3 file.
    """
    try:
        program_path = '{}/{}'.format(settings.MEDIA_ROOT, obj.file.name)
        return int(math.ceil(MP3(program_path).info.length))

    except Exception:
        return None


def get_minutes_and_seconds(duration):
    """
    Get duration as tuple (minutes, seconds).

    Minutes and seconds are both integers.
    """
    minutes = duration // 60
    seconds = duration % 60
    return (minutes, seconds)


def get_printable_duration(duration):
    """
    Get duration as string in format min'sec"
    """
    minutes, seconds = get_minutes_and_seconds(duration)
    return u'{0}{1}{2:02d}{3}'.format(
        minutes, u'\N{PRIME}', seconds, u'\N{DOUBLE PRIME}')


class Creation(models.Model, RealInstanceProvider):
    """Superclass for one of Laura's creations."""

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,
                                   help_text=settings.MARKDOWN_PROMPT)
    species = models.ManyToManyField(Species, blank=True,
                                     limit_choices_to={'is_visible': True})
    tags = TaggableManager(blank=True)
    is_favorite = models.BooleanField(default=False)
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
                (str(a) for a in ancestors))

        else:
            class_name = self.__class__.__name__
            words = re.findall('[A-Z][^A-Z]*', class_name)
            return ' '.join(words)

    def get_display_date(self):
        if hasattr(self, 'date_published'):
            return self.date_published
        elif hasattr(self, 'date_recorded'):
            return self.date_recorded
        elif hasattr(self, 'air_date'):
            return self.air_date
        else:
            return None

    def is_research(self):
        class_name = self.__class__.__name__
        return class_name.lower() == 'research'

    def is_radio_program(self):
        class_name = self.get_actual_instance().__class__.__name__
        return class_name.lower().startswith('radio')

    def has_tags(self):
        return len(self.species.all()) or len(self.tags.names())


class Article(Creation):
    """An article written by Laura."""

    published_by = models.CharField(max_length=100, blank=True)
    date_published = models.DateField(null=True, blank=True)
    url = models.URLField(blank=True)
    file = models.FileField(null=True, blank=True, upload_to='articles')
    text = models.TextField(blank=True, help_text=settings.MARKDOWN_PROMPT)

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return u'Article: {}'.format(self.title)

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
        return u'Blog Post: {}'.format(self.title)

    def get_absolute_url(self):
        return self.url


class Book(Creation):
    """A book written by Laura."""

    slug = models.SlugField(max_length=120, unique=True)
    published_by = models.CharField(max_length=100, blank=True)
    date_published = models.DateField(null=True, blank=True)
    purchase_url = models.URLField(blank=True)
    cover_photo = models.ForeignKey(
        UploadedImage, models.SET_NULL, null=True, blank=True)
    isbn_10 = models.CharField('ISBN 10', max_length=20, blank=True)
    isbn_13 = models.CharField('ISBN 13', max_length=20, blank=True)

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return u'Book: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('book_url', args=[self.slug])


class ExternalProject(Creation):
    """One of Laura's projects hosted on an external domain."""

    url = models.URLField()
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'title']

    def __unicode__(self):
        return u'External Project: {}'.format(self.title)

    def get_absolute_url(self):
        return self.url


class RadioProgram(Creation):
    """A 'For the Birds' radio program."""

    file = models.FileField(upload_to='radio', blank=True)

    # Duration in seconds
    duration = models.PositiveIntegerField(blank=True, null=True)

    air_date = models.DateField()
    date_is_estimate = models.BooleanField(default=False)
    blog_url = models.URLField(blank=True)
    transcript = models.TextField(blank=True,
                                  help_text=settings.MARKDOWN_PROMPT)

    class Meta:
        ordering = ['-air_date']

    def __unicode__(self):
        return u'Radio Program: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('radio_program_url',
                       args=[self.id, slugify(self.title)])

    def has_file(self):
        return self.file != ''
    has_file.boolean = True

    def has_blog_url(self):
        return self.blog_url != ''
    has_blog_url.boolean = True

    def has_transcript(self):
        return self.transcript != ''
    has_transcript.boolean = True

    def get_reruns(self):
        """
        Get all reruns of this program.
        """
        return self.radioprogramrerun_set.all()

    def get_number_of_reruns(self):
        """
        Get the number of reruns for this program.
        """
        return len(self.get_reruns())
    get_number_of_reruns.short_description = 'Num reruns'

    def get_artwork(self):
        """
        Get artwork embedded in this program's mp3 file.
        """
        return get_artwork_from_file(self)

    def get_printable_duration(self):
        """
        Get duration as string in format min'sec"
        """
        if self.duration:
            return get_printable_duration(self.duration)
        else:
            return 'N/A'

    def get_itunes_duration(self):
        """
        Get program duration as string in format min:sec
        """
        if self.duration:
            minutes, seconds = get_minutes_and_seconds(self.duration)
            return '{}:{:02d}'.format(minutes, seconds)
        else:
            return '0:00'


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
    post_save.disconnect(add_radio_program_duration, sender=sender)
    instance.duration = get_duration_from_file(instance)
    instance.save()
    post_save.connect(add_radio_program_duration, sender=sender)


class RadioProgramRerun(models.Model):
    """A rerun airing of a RadioProgram."""

    program = models.ForeignKey(RadioProgram, models.CASCADE)
    air_date = models.DateField()

    class Meta:
        ordering = ['-air_date']

    def __unicode__(self):
        return u'{} aired {}'.format(self.program, self.air_date)


class RadioProgramMissedDate(models.Model):
    """
    A date that Laura forgot to put up a radio program.

    This is useful only for "filling up" archived calendars.
    """

    text = models.CharField(max_length=255)
    air_date = models.DateField()

    class Meta:
        ordering = ['-air_date']


class ResearchCategory(models.Model):
    """A category of Laura's private research."""

    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, help_text=settings.MARKDOWN_PROMPT)
    parent = models.ForeignKey(
        'self', models.SET_NULL, null=True, blank=True)

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
    """A (typically) private research item of Laura's."""

    category = models.ForeignKey(ResearchCategory, models.CASCADE)
    is_public = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    attribution = models.CharField(max_length=200, blank=True,
                                   help_text=settings.MARKDOWN_PROMPT)
    url = models.URLField(blank=True)
    file = models.FileField(null=True, blank=True, upload_to='research')
    text = models.TextField(blank=True, help_text=settings.MARKDOWN_PROMPT)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Research'

    def __unicode__(self):
        return u'Research: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('research_item_url', args=[self.id])

    def get_ancestors(self):
        ancestors = [self.category]
        ancestors.extend(self.category.get_ancestors())
        return ancestors


class SoundRecording(Creation):
    """A bird sound recording."""

    file = models.FileField(upload_to='soundrecordings')

    # Duration in seconds
    duration = models.PositiveIntegerField(blank=True, null=True)

    date_recorded = models.DateField()
    location = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-date_recorded']

    def __unicode__(self):
        return u'Sound Recording: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('sound_recording_url', args=[self.id])

    def get_artwork(self):
        """
        Get artwork embedded in this program's mp3 file.
        """
        return get_artwork_from_file(self)

    def get_printable_duration(self):
        """
        Get duration as string in format min'sec"
        """
        if self.duration:
            return get_printable_duration(self.duration)
        else:
            return 'N/A'


@receiver(post_save, sender=SoundRecording)
def add_sound_recording_duration(sender, instance, **kwargs):
    """
    Signal handler to set sound recording duration after it is saved.

    See similar RadioProgram signal handler for more details.
    """
    post_save.disconnect(add_sound_recording_duration, sender=sender)
    instance.duration = get_duration_from_file(instance)
    instance.save()
    post_save.connect(add_sound_recording_duration, sender=sender)


class SpeakingProgram(Creation):
    """A public speaking program."""

    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return u'Speaking Program: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('speaking_program_url', args=[self.slug])


class WebPage(Creation):
    """A static web page of Laura's to be displayed within this website."""

    slug = models.SlugField(max_length=120, unique=True)
    date_published = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True, help_text=settings.MARKDOWN_PROMPT)
    is_public = models.BooleanField(default=True)
    display_title = models.BooleanField(default=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'title']

    def __unicode__(self):
        return u'Web Page: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('webpage_url', args=[self.slug])
