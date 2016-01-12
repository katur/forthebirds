# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0009_species_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
