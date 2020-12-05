import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from forthebirds.localsettings import FLICKR_USER_ID


register = template.Library()


@register.filter
def is_string_equal(x, y):
    return str(x) == str(y)


@register.filter(is_safe=True)
@stringfilter
def enhanced_markdown(value):
    extensions = [
        'smarty',  # emdash, endash, pretty quotes
    ]

    return mark_safe(markdown.markdown(
        force_text(value), extensions=extensions))


@register.filter
def is_flickr_src(src):
    return 'staticflickr' in src


@register.filter
def get_flickr_url_from_flickr_src(src):
    photo_id = src.split('/')[-1].split('_')[0]
    return 'https://www.flickr.com/photos/{}/{}'.format(FLICKR_USER_ID,
                                                        photo_id)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
