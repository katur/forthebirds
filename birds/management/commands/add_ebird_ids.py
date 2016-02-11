import argparse

from django.core.management.base import BaseCommand

from birds.models import Species

import csv


class Command(BaseCommand):
    help = ('Populate new ebird_id column. First step of migrating from '
            'NACC/AOU database to eBird database.')

    def add_arguments(self, parser):
        parser.add_argument('ebird_csv', type=argparse.FileType('r'),
                            help='CSV of species data from eBird')

    def handle(self, **options):
        # Create mappings from ebird common and scientific names to ebird_id
        common_to_ebird = {}
        scientific_to_ebird = {}

        for row in csv.DictReader(options['ebird_csv']):
            if row['CATEGORY'] != 'species':
                continue

            ebird_id = row['SPECIES_CODE']
            common_to_ebird[row['PRIMARY_COM_NAME']] = ebird_id
            scientific_to_ebird[row['SCI_NAME']] = ebird_id

        # For each bird in the database, add the ebird_id
        for bird in Species.objects.all():
            if (bird.common_name not in common_to_ebird and
                    bird.scientific_name not in scientific_to_ebird):
                self.stderr.write('{} missing ENTIRELY'
                                  .format(bird))

                # Only delete individually verified cases
                if bird.common_name == 'Greater Akialoa':
                    bird.delete()

                continue

            elif bird.common_name in common_to_ebird:
                bird.ebird_id = common_to_ebird[bird.common_name]

            else:
                bird.ebird_id = scientific_to_ebird[bird.scientific_name]

            bird.save()
