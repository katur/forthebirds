# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0003_remove_species_is_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='main_photo_url',
            field=models.URLField(blank=True),
        ),
    ]
