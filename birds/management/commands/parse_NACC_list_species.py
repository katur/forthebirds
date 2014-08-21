from django.core.management.base import BaseCommand

from birds.models import TaxonomicLevel, TaxonomicGroup, Species

import csv


expected_fields = (
    'id', 'rank',
    'order', 'family', 'subfamily', 'genus', 'species',
    'common_name', 'french_name',
    'annotation',
    'status_accidental', 'status_hawaiian', 'status_introduced',
    'status_nonbreeding', 'status_extinct', 'status_misplaced',
)


required_fields = (
    'id', 'rank',
    'order', 'family', 'genus', 'species',
    'common_name', 'french_name',
)

expected_levels = ('order', 'family', 'subfamily', 'genus')


def confirm_expected_fields_present(header):
    for field in expected_fields:
        if field not in header:
            raise Exception(
                'Expected field `' + field + '` is missing from header')

    if set(header) - set(expected_fields):
        print 'Warning: extra fields present in input:'
        print [i for i in set(header) - set(expected_fields)]

    return


def confirm_required_fields_present(row):
    if not row['common_name']:
        raise Exception('some common name missing')

    for field in required_fields:
        if not row[field]:
            raise Exception(field + ' missing in ' + row['common_name'])

    return


def confirm_rank_is_species(row):
    if row['rank'] != 'species':
        print 'Warning: rank != "species" for ' + row['common_name']


def update_max_field_widths(row, fieldnames, max_field_widths):
    for field in fieldnames:
        if row[field] and (
                field not in max_field_widths
                or len(row[field]) > max_field_widths[field]):
            max_field_widths[field] = len(row[field])


def get_taxonomic_level_dictionary():
    levels = {}

    for level in expected_levels:
        try:
            level_object = TaxonomicLevel.objects.get(name=level)
            levels[level] = level_object
        except TaxonomicLevel.DoesNotExist:
            raise Exception(
                'Expected taxonomic level ' + level + ' not in database')

    return levels


class Command(BaseCommand):
    """
    Run as: ./manage.py parse_NACC_list_species filename.csv
    """
    help = 'Populate Bird taxonomy tables from official NACC list'

    def handle(self, *args, **options):
        filename = args[0]
        levels = get_taxonomic_level_dictionary()
        max_field_widths = {}

        with open(filename, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            confirm_expected_fields_present(fieldnames)

            unknown = '<i>Incertae Sedis</i>'
            unknown_counter = 0
            previous_row = None

            for row in reader:
                confirm_rank_is_species(row)
                confirm_required_fields_present(row)

                for field, value in row.iteritems():
                    if unknown in value:
                        if unknown not in previous_row[field]:
                            unknown_counter += 1
                            row[field] = unknown + str(unknown_counter)
                        else:
                            row[field] = previous_row[field]

                update_max_field_widths(row, fieldnames, max_field_widths)

                current_parent = None
                for level in expected_levels:
                    if not row[level]:
                        continue

                    if not current_parent and level != 'order':
                        raise Exception('non-Order level should have a parent')

                    '''
                    if previous_row and (row[level] != previous_row[level]):
                        if TaxonomicGroup.objects.filter(
                            name=row[level]
                        ).exists():
                            print 'warning: ' + row[level] + ' exists already'
                    '''

                    try:
                        group = TaxonomicGroup.objects.get(
                            name=row[level],
                            level=levels[level],
                            parent=current_parent
                        )

                    except TaxonomicGroup.DoesNotExist:
                        group = TaxonomicGroup(
                            name=row[level],
                            level=levels[level],
                            parent=current_parent
                        )
                        group.save()

                    current_parent = group

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
                        parent=current_parent,
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

                previous_row = row
