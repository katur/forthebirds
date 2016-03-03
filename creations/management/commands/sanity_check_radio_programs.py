import re

from django.core.management.base import BaseCommand

from creations.models import RadioProgram


class Command(BaseCommand):
    help = ('Find radio programs with filename naming inconsistencies')

    def handle(self, **options):
        for p in RadioProgram.objects.all():
            if not re.match(r'^radio/\d\d\d\d\-\d\d\-\d\d_[^_]*$',
                            p.file.name):
                self.stderr.write('{} mismatches'.format(p.file.name))
