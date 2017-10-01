from datetime import datetime, date, time

from django.conf import settings
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils.feedgenerator import Rss201rev2Feed

from creations.models import RadioProgram
from utils.http import https_to_http

EPISODE_LIMIT = 250

HOME_URL = https_to_http(settings.SITE_DOMAIN)
RADIO_URL = https_to_http('{}/radio/'.format(settings.SITE_DOMAIN))
FEED_URL = https_to_http('{}/radio/feed.xml'.format(settings.SITE_DOMAIN))
AUTHOR_IMAGE_URL = https_to_http((
    '{}images/a588d7c7-cb24-487b-bf3e-b8e94b61fb72_'
    'laura_erickson_itunes.jpg'
).format(settings.MEDIA_URL))

class iTunesFeed(Rss201rev2Feed):
    """
    From https://djangosnippets.org/snippets/2112/
    """

    def rss_attributes(self):
        super(iTunesFeed, self).rss_attributes()
        return {
            'version': self._version,
            'xml:lang': 'en-us',
            'xmlns:atom': 'http://www.w3.org/2005/Atom',
            'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        }

    def add_root_elements(self, handler):
        super(iTunesFeed, self).add_root_elements(handler)

        handler.addQuickElement('itunes:new-feed-url',
                                self.feed['itunes_new_feed_url'])
        handler.addQuickElement('itunes:image', '',
                                {'href': self.feed['itunes_image_url']})
        handler.addQuickElement('itunes:summary',
                                self.feed['description'])
        handler.addQuickElement('itunes:subtitle',
                                self.feed['subtitle'])
        handler.addQuickElement('itunes:author',
                                self.feed['author_name'])

        handler.startElement('itunes:owner', {})
        handler.addQuickElement('itunes:name',
                                self.feed['itunes_name'])
        handler.addQuickElement('itunes:email',
                                self.feed['itunes_email'])
        handler.endElement('itunes:owner')

        handler.addQuickElement('itunes:explicit',
                                self.feed['itunes_explicit'])

        for outer, inners in self.feed['itunes_categories'].items():
            handler.startElement('itunes:category', {'text': outer})
            for inner in inners:
                handler.addQuickElement('itunes:category', '',
                                        {'text': inner})
            handler.endElement('itunes:category')

    def add_item_elements(self, handler, item):
        super(iTunesFeed, self).add_item_elements(handler, item)
        handler.addQuickElement('itunes:summary', item['description'])
        handler.addQuickElement('itunes:explicit', item['itunes_explicit'])
        handler.addQuickElement('itunes:duration', item['itunes_duration'])


class ForTheBirdsPodcastFeed(Feed):
    """
    Feed for For The Birds iTunes podcast.
    """

    feed_type = iTunesFeed
    title = "Laura Erickson's For the Birds"
    subtitle = 'For the love, understanding, and protection of birds.'
    link = RADIO_URL
    feed_url = FEED_URL

    description = (
        '"For the Birds" began airing on KUMD in Duluth, MN, in May, 1986, '
        'and is the longest continually-running radio '
        'program about birds in the U.S. '
        'Hundreds more episodes are available for free at {}.'
    ).format(RADIO_URL)

    author_name = 'Laura Erickson'
    author_email = 'chickadee@lauraerickson.com'
    author_link = HOME_URL

    feed_copyright = 'Copyright {} by Laura Erickson'.format(
        date.today().year)

    def feed_extra_kwargs(self, obj):
        extras = {}
        extras['itunes_name'] = 'Laura Erickson'
        extras['itunes_email'] = 'chickadee@lauraerickson.com'
        extras['itunes_new_feed_url'] = FEED_URL
        extras['itunes_image_url'] = AUTHOR_IMAGE_URL
        extras['itunes_explicit'] = 'clean'
        extras['itunes_categories'] = {
            'Science &amp; Medicine': ['Natural Sciences'],
            'Society &amp; Culture': ['Places &amp; Travel'],
            'Sports &amp; Recreation': ['Outdoor'],
        }
        return extras

    def items(self):
        """Get a list of items to publish in this feed."""
        today = datetime.today()
        return (RadioProgram.objects.order_by('-air_date')
                .filter(air_date__lte=today)
                .exclude(file='')
                )[:EPISODE_LIMIT]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return datetime.combine(item.air_date, time())

    def item_link(self, item):
        return https_to_http('{}{}'.format(
            settings.SITE_DOMAIN,
            reverse('radio_program_url',
                    args=[item.pk, slugify(item.title)])
        ))

    def item_enclosure_url(self, item):
        # The mp3 URL
        return https_to_http(item.file.url)

    def item_enclosure_length(self, item):
        try:
            return item.file.size
        except OSError:
            return 0

    def item_enclosure_mime_type(self, item):
        return 'audio/mpeg'

    def item_extra_kwargs(self, item):
        return {
            'itunes_explicit': 'clean',
            'itunes_duration': item.get_itunes_duration(),
        }
