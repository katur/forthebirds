import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def is_string_equal(x, y):
    return str(x) == str(y)


@register.filter(is_safe=True)
@stringfilter
def enhanced_markdown(value):
    extensions = [
        'nl2br',  # more intuitive linebreak
        'smarty',  # emdash, endash, pretty quotes
    ]

    return mark_safe(markdown.markdown(
        force_unicode(value), extensions, enable_attributes=False))
