# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0006_remove_species_bird_of_the_week_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='has_abc_bird_of_the_week_url',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='species',
            name='has_cornell_all_about_birds_url',
            field=models.BooleanField(default=False),
        ),
    ]
