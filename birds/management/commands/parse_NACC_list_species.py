from django.core.management.base import BaseCommand

from birds.models import Order, Family, Subfamily, Genus, Species

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


def confirm_species_rank(row):
    if row['rank'] != 'species':
        print 'Warning: rank != "species" for ' + row['common_name']


def update_max_field_widths(row, fieldnames, max_field_widths):
    for field in fieldnames:
        if row[field] and (
                field not in max_field_widths
                or len(row[field]) > max_field_widths[field]):
            max_field_widths[field] = len(row[field])


class Command(BaseCommand):
    """
    Run as: ./manage.py parse_NACC_list_species filename.csv
    """
    help = 'Populate Bird taxonomy tables from official NACC list'

    def handle(self, *args, **options):
        filename = args[0]
        max_field_widths = {}
        subfamily_count = 0
        no_subfamily = 0

        with open(filename, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            confirm_expected_fields_present(fieldnames)
            for row in reader:
                confirm_species_rank(row)
                confirm_required_fields_present(row)
                update_max_field_widths(row, fieldnames, max_field_widths)

                try:
                    order = Order.objects.get(name=row['order'])
                except Order.DoesNotExist:
                    order = Order(name=row['order'])
                    order.save()

                try:
                    family = Family.objects.get(name=row['family'])
                    if family.order != order:
                        raise Exception(
                            'Order does not match for family ' + str(family)
                        )
                except Family.DoesNotExist:
                    family = Family(name=row['family'], order=order)
                    family.save()

                if row['subfamily']:
                    subfamily_count += 1
                else:
                    no_subfamily += 1

            print subfamily_count
            print no_subfamily
