from django.core.management.base import BaseCommand

from birds.models import TaxonomicLevel, TaxonomicGroup, Species

import csv


class Command(BaseCommand):
    """
    Run as: ./manage.py parse_NACC_list_species filename.csv
    """
    help = 'Populate Bird taxonomy tables from official NACC list'

    def handle(self, *args, **options):
        filename = args[0]
        levels = get_taxonomic_level_objects()
        max_field_widths = {}

        with open(filename, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            confirm_expected_header_fields(fieldnames)

            previous_row = None
            for row in reader:
                confirm_proper_row(row)
                update_UNCERTAIN_fields(row, previous_row)
                update_max_field_widths(row, fieldnames, max_field_widths)
                parent = update_ancestors(row, previous_row, levels)
                update_species(row, parent)
                previous_row = row


def get_taxonomic_level_objects():
    levels = []
    for level_string in ('order', 'family', 'subfamily', 'genus'):
        try:
            level_object = TaxonomicLevel.objects.get(name=level_string)
            levels.append(level_object)
        except TaxonomicLevel.DoesNotExist:
            raise Exception('Expected taxonomic level ' + level_string +
                            ' not in database')
    return levels


def confirm_expected_header_fields(header):
    EXPECTED_FIELDS = (
        'id', 'rank', 'order', 'family', 'subfamily', 'genus', 'species',
        'common_name', 'french_name', 'annotation',
        'status_accidental', 'status_hawaiian', 'status_introduced',
        'status_nonbreeding', 'status_extinct', 'status_misplaced',
    )

    for field in EXPECTED_FIELDS:
        if field not in header:
            raise Exception(
                'Expected field `' + field + '` missing from header')

    if set(header) - set(EXPECTED_FIELDS):
        print 'Warning: extra fields present in header: '
        print [i for i in set(header) - set(EXPECTED_FIELDS)]

    return


def confirm_proper_row(row):
    if not row['id']:
        raise Exception('some id missing!')

    REQUIRED_FIELDS = (
        'id', 'rank',
        'order', 'family', 'genus', 'species',
        'common_name', 'french_name',
    )

    for field in REQUIRED_FIELDS:
        if not row[field]:
            raise Exception(field + ' missing for bird id ' + row['id'])

    if row['rank'] != 'species':
        print 'Warning: rank != "species" for bird id ' + row['id']

    return


def update_max_field_widths(row, fieldnames, max_field_widths):
    for field in fieldnames:
        if row[field] and (
                field not in max_field_widths
                or len(row[field]) > max_field_widths[field]):
            max_field_widths[field] = len(row[field])


def update_UNCERTAIN_fields(row, previous_row):
    UNCERTAIN_IN_LATIN = '<i>Incertae Sedis</i>'
    for field, value in row.iteritems():
        if UNCERTAIN_IN_LATIN in value:
            if UNCERTAIN_IN_LATIN not in previous_row[field]:
                update_UNCERTAIN_fields.counter += 1
                row[field] = (UNCERTAIN_IN_LATIN +
                              str(update_UNCERTAIN_fields.counter))
            else:
                row[field] = previous_row[field]

update_UNCERTAIN_fields.counter = 0


def update_ancestors(row, previous_row, levels):
    current_parent = None
    for level in levels:
        if not row[level.name]:
            continue

        if not current_parent and level.depth > 1:
            raise Exception('levels of depth > 1 require parent')

        try:
            group = TaxonomicGroup.objects.get(
                name=row[level.name],
            )

            if group.level != level:
                print ('Warning: group {0} changing level from '
                       '{1} to {2} (see bird id {3})'
                       .format(
                           str(group),
                           str(group.level),
                           str(level),
                           row['id'],
                       ))
                group.level = level
                group.save()

            if group.parent != current_parent:
                print ('Warning: group {0} changing parent from '
                       '{1} to {2} (see bird id {3})'
                       .format(
                           str(group),
                           str(group.parent),
                           str(current_parent),
                           row['id'],
                       ))
                group.parent = current_parent
                group.save()

        except TaxonomicGroup.DoesNotExist:
            group = TaxonomicGroup(
                name=row[level.name],
                level=level,
                parent=current_parent
            )
            group.save()

        current_parent = group

    return current_parent


def update_species(row, parent):
    try:
        species = Species.objects.get(
            id=row['id']
        )
        if (species.name != row['species'] or
                species.common_name != row['common_name']):
            print 'warning: species ' + str(species) + ' issue'

    except Species.DoesNotExist:
        species = Species(
            id=row['id'],
            parent=parent,
            name=row['species'],
            common_name=row['common_name'],
            french_name=row['french_name'],
            nacc_annotation=row['annotation'],
            nacc_is_accidental=bool(row['status_accidental']),
            nacc_is_hawaiian=bool(row['status_hawaiian']),
            nacc_is_introduced=bool(row['status_introduced']),
            nacc_is_nonbreeding=bool(row['status_nonbreeding']),
            nacc_is_extinct=bool(row['status_extinct']),
            nacc_is_misplaced=bool(row['status_misplaced']),
        )
        species.save()
