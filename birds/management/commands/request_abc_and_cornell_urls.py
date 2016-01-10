from django.core.management.base import BaseCommand

from birds.models import Species
from utils.scripting import require_db_write_acknowledgement


class Command(BaseCommand):
    help = ('Determine ABC bird of the week and Cornell all about birds '
            'url fields')

    def handle(self, **options):
        require_db_write_acknowledgement()

        birds = Species.objects.all()
        for bird in birds:
            abc = bird.get_resolved_abc_bird_of_the_week_url()
            if abc:
                bird.has_abc_bird_of_the_week_url = True

            cornell = bird.get_resolved_cornell_all_about_birds_url()
            if cornell:
                bird.has_cornell_all_about_birds_url = True

            bird.save()
