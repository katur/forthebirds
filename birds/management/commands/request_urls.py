from django.core.management.base import BaseCommand

from birds.models import Species
from utils.scripting import require_db_write_acknowledgement


class Command(BaseCommand):
    help = ('Determine Wikipedia, ABC Bird of the Week, and Cornell All '
            'About Birds url fields')

    def handle(self, **options):
        require_db_write_acknowledgement()

        for bird in Species.objects.filter(is_visible=True):
            self.stdout.write('Processing bird {}'.format(bird))

            cornell = bird.get_resolved_cornell_all_about_birds_url()
            if cornell and not bird.has_cornell_all_about_birds_url:
                bird.has_cornell_all_about_birds_url = True
                bird.save()
                self.stdout.write('\tAdded Cornell url for {}'.format(bird))

            elif not cornell and bird.has_cornell_all_about_birds_url:
                self.stderr.write('\tWARNING: Cornell lookup failed for {}'
                                  .format(bird))

            wiki = bird.get_resolved_wikipedia_url()
            if wiki and not bird.has_wikipedia_url:
                bird.has_wikipedia_url = True
                bird.save()
                self.stdout.write('\tAdded Wikipedia url for {}'.format(bird))

            elif not wiki and bird.has_wikipedia_url:
                self.stderr.write('\tWARNING: Wikipedia lookup failed for {}'
                                  .format(bird))

            mn = bird.get_resolved_mn_bird_atlas_url()
            if mn and not bird.has_mn_bird_atlas_url:
                bird.has_mn_bird_atlas_url = True
                bird.save()
                self.stdout.write('\tAdded MN Bird Atlas url for {}'.format(bird))

            elif not mn and bird.has_mn_bird_atlas_url:
                self.stderr.write('\tWARNING: MN Bird Atlas lookup failed for {}'
                                  .format(bird))
