import re

from django.core.management.base import BaseCommand

from creations.models import RadioProgram, SoundRecording


class Command(BaseCommand):
    help = ('Find radio programs with filename naming inconsistencies')

    def handle(self, **options):
        for p in RadioProgram.objects.all():
            if not _is_properly_named('radio', p.file.name):
                self.stderr.write('{} improper'.format(p.file.name))

        for s in SoundRecording.objects.all():
            if not _is_properly_named('soundrecordings', s.file.name):
                self.stderr.write('{} improper'.format(s.file.name))


def _is_properly_named(directory, filename):
    return re.match(r'^{}/\d\d\d\d\-\d\d\-\d\d_[^_]*$'.format(directory),
                    filename)
