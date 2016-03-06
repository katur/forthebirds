from django.contrib import admin


class NullListFilter(admin.SimpleListFilter):
    """
    Admin list filter to filter for whether a field is null or not null.
    """

    def lookups(self, request, model_admin):
        return (('0', 'Not None',), ('1', 'None',),)

    def queryset(self, request, queryset):
        if self.value() in ('0', '1'):
            kwargs = {
                '{}__isnull'.format(self.parameter_name): self.value() == '1'
            }
            return queryset.filter(**kwargs)
        return queryset


def null_filter(field, title_=None):
    """
    Helper function to create a NullListFilter for a particular field.

    Sets the parameter_name and title to the field being filtered on.
    """
    class NullListFieldFilter(NullListFilter):

        parameter_name = field
        title = title_ or parameter_name

    return NullListFieldFilter


class EmptyListFilter(admin.SimpleListFilter):
    """
    Admin list filter to filter for whether a field is empty or not empty.
    """

    def lookups(self, request, model_admin):
        return (('0', 'Not None',), ('1', 'None', ),)

    def queryset(self, request, queryset):
        kwargs = {'{}__exact'.format(self.parameter_name): ''}

        if self.value() == '1':
            return queryset.filter(**kwargs)
        elif self.value() == '0':
            return queryset.exclude(**kwargs)

        else:
            return queryset


def empty_filter(field, title_=None):
    """
    Helper function to create a EmptyListFilter for a particular field.

    Sets the parameter_name and title to the field being filtered on.
    """
    class EmptyListFieldFilter(EmptyListFilter):

        parameter_name = field
        title = title_ or parameter_name

    return EmptyListFieldFilter
