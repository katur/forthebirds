import re

from django.core.urlresolvers import reverse
from django.db import models

from taggit.managers import TaggableManager
from private_media.storages import PrivateMediaStorage

from forthebirds.settings import MARKDOWN_PROMPT
from birds.models import Species
from website.models import UploadedImage
from utils.models import RealInstanceProvider


class Creation(models.Model, RealInstanceProvider):
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
            return u'\u2192'.join((unicode(a) for a in ancestors))

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
        return len(self.species) or len(self.tags.names())


class RadioProgram(Creation):
    original_air_date = models.DateField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='radio')
    supplemental_content_url = models.URLField(blank=True)
    transcript = models.TextField(blank=True,
                                  help_text=MARKDOWN_PROMPT)

    class Meta:
        ordering = ['-original_air_date']

    def __unicode__(self):
        return 'Radio Program: ' + self.title

    def get_absolute_url(self):
        return reverse('creations.views.radio_program', args=[self.id])

    def get_display_date(self):
        return self.original_air_date

    def get_reruns(self):
        return self.radioprogramrerun_set


class RadioProgramRerun(models.Model):
    program = models.ForeignKey(RadioProgram)
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return '{} aired {}'.format(self.program, self.date)


class Book(Creation):
    purchase_url = models.URLField(blank=True)
    cover_photo = models.ForeignKey(UploadedImage, null=True, blank=True,
                                    on_delete=models.SET_NULL)
    publisher = models.CharField(max_length=100, blank=True)
    isbn_10 = models.CharField('ISBN 10', max_length=20, blank=True)
    isbn_13 = models.CharField('ISBN 13', max_length=20, blank=True)
    date_published = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return 'Book: ' + self.title

    def get_absolute_url(self):
        return reverse('creations.views.book', args=[self.id])


class Article(Creation):
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
        return reverse('creations.views.article', args=[self.id])


class SpeakingProgram(Creation):
    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return 'Speaking Program: ' + self.title

    def get_absolute_url(self):
        return reverse('creations.views.speaking_program', args=[self.id])


class SpeakingProgramFile(models.Model):
    program = models.ForeignKey(SpeakingProgram)
    title = models.CharField(max_length=120)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)
    file = models.FileField(null=True, blank=True, upload_to='speaking',
                            storage=PrivateMediaStorage())

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return 'Speaking Presentation File: ' + self.title

    def get_absolute_url(self):
        return self.file.url


class BlogPost(Creation):
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return 'Blog Post: ' + self.title

    def get_absolute_url(self):
        return self.url


class WebPage(Creation):
    slug = models.SlugField(max_length=255)
    date_published = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return 'Web Page: ' + self.title

    def get_absolute_url(self):
        return reverse('creations.views.webpage', args=[self.slug])


class ExternalProject(Creation):
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return 'External Project: ' + self.title

    def get_absolute_url(self):
        return self.url


class ResearchCategory(models.Model):
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
        return reverse('creations.views.research_category', args=[self.id])

    def get_ancestors(self):
        ancestors = []
        parent = self.parent
        while parent:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors


class Research(Creation):
    category = models.ForeignKey(ResearchCategory)
    date = models.DateField(null=True, blank=True)
    attribution = models.CharField(max_length=200, blank=True,
                                   help_text=MARKDOWN_PROMPT)
    url = models.URLField(blank=True)
    file = models.FileField(null=True, blank=True, upload_to='research')
    text = models.TextField(blank=True, help_text=MARKDOWN_PROMPT)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Research'

    def __unicode__(self):
        return 'Research: ' + self.title

    def get_absolute_url(self):
        return reverse('creations.views.research', args=[self.id])

    def get_ancestors(self):
        ancestors = [self.category]
        ancestors.extend(self.category.get_ancestors())
        return ancestors


class ABAFieldGuideImage(Creation):
    image = models.ImageField(null=True, blank=True, upload_to='abafieldguide')
    is_public = False
    is_image = True

    class Meta:
        ordering = ['title']
        verbose_name = 'ABA Field Guide Image'
        verbose_name = 'ABA Field Guide Images'

    def __unicode__(self):
        return 'ABA Field Guide Image ' + self.title

    def get_absolute_url(self):
        return self.image.url
