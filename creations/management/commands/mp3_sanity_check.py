import re

from django.core.management.base import BaseCommand

from creations.models import RadioProgram, SoundRecording


class Command(BaseCommand):
    help = ('Find radio programs with filename naming inconsistencies')

    def handle(self, **options):
        for p in RadioProgram.objects.all():
            if not _is_properly_named('radio', p.file.name):
                self.stderr.write('IMPROPER: {}'.format(p.file.name))

            if not _dates_match(p.file.name, p.air_date):
                self.stderr.write('DATE MISMATCH: {}'.format(p.file.name))

        for s in SoundRecording.objects.all():
            if not _is_properly_named('soundrecordings', s.file.name):
                self.stderr.write('IMPROPER: {}'.format(s.file.name))

            if not _dates_match(s.file.name, s.date_recorded):
                self.stderr.write('DATE MISMATCH: {}'.format(s.file.name))


def _is_properly_named(directory, filename):
    return re.match(r'^{}/\d\d\d\d\-\d\d\-\d\d_[^_]*$'.format(directory),
                    filename)


def _dates_match(filename, date):
    return filename.split('/')[1][:10] == str(date)
