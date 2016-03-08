import os.path
import re

from django.conf import settings
from django.core.management.base import BaseCommand

from creations.models import RadioProgram, SoundRecording


class Command(BaseCommand):
    help = ('Find radio programs with filename naming inconsistencies')

    def handle(self, **options):
        for p in RadioProgram.objects.all():
            _perform_sanity_checks(p.file.name, p.air_date, self)

        for s in SoundRecording.objects.all():
            _perform_sanity_checks(s.file.name, s.date_recorded, self)


def _perform_sanity_checks(filename, date, stream):
    if not _file_exists(filename):
        stream.stderr.write('FILE DOES NOT EXIST: {}'.format(filename))

    if not _is_properly_named(filename):
        stream.stderr.write('IMPROPER FILENAME: {}'.format(filename))

    if not _dates_match(filename, date):
        stream.stderr.write('DATE MISMATCH: {} (database says {})'.format(
            filename, date))


def _file_exists(filename):
    return os.path.isfile(settings.MEDIA_ROOT + '/' + filename)


def _is_properly_named(filename):
    return re.match(r'^\d\d\d\d\-\d\d\-\d\d_[^_]*$', filename.split('/')[1])


def _dates_match(filename, date):
    return filename.split('/')[1][:10] == str(date)
