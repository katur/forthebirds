from creations.models import RadioProgram

programs = RadioProgram.objects.all()

for program in programs:
    program.original_air_date = program.orig_air_date.date
    program.save()
