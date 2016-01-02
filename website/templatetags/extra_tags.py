from django import template

register = template.Library()


@register.filter
def is_string_equal(x, y):
    return str(x) == str(y)
