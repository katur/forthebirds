import os
import re
import sys

from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.core.management.base import BaseCommand

from birds.models import Species
from creations.models import ABAFieldGuideImage


class Command(BaseCommand):
    """
    Run as: ./manage.py add_field_guide_pics path_to_images
    """
    help = 'Add field guide pictures to database'

    def handle(self, *args, **options):
        try:
            dropbox_path = args[0]
        except IndexError:
            print ('Incorrect usage. Correct usage: '
                   './manage.py add_field_guide_pics path_to_images')
            sys.exit(2)

        image_filenames = os.listdir(dropbox_path)
        for image_filename in image_filenames:
            common_name = image_filename.rpartition('.jpg')[0]

            # Remove trailing whitespace
            common_name = common_name.rstrip()

            if '_' in common_name:
                common_name = common_name.partition('_')[0]
            else:
                common_name = re.split('[0-9]+', common_name)[0]

            if common_name.endswith(' copy'):
                common_name = common_name.rpartition(' copy')[0]

            if common_name.endswith(' vertical'):
                common_name = common_name.rpartition(' vertical')[0]

            if '(' in common_name:
                common_name = common_name.partition('(')[0]

            # Remove trailing whitespace
            common_name = common_name.rstrip()

            try:
                species = Species.objects.get(common_name=common_name)

            except ObjectDoesNotExist:
                print('Skipping ' + image_filename + ' (no matching species)')
                continue

            try:
                image = ABAFieldGuideImage.objects.get(
                    title=image_filename)

            except ObjectDoesNotExist:
                image = ABAFieldGuideImage(title=image_filename)

            if not image.image:
                f = open(dropbox_path + '/' + image_filename)
                image.image.save(image_filename, File(f), save=True)

            if species not in image.species.all():
                image.species.add(species)
