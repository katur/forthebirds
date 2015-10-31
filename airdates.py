from django.core.exceptions import ObjectDoesNotExist
from creations.models import RadioProgram, RadioProgramAirDate

programs = RadioProgram.objects.all()

for program in programs:
    try:
        RadioProgramAirDate.objects.get(program=program)
    except ObjectDoesNotExist:
        x = RadioProgramAirDate(program=program,
                                date=program.old_air_date)
        x.save()
        program.original_air_date = x
        program.save()
