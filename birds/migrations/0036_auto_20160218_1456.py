# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0035_species_has_wikipedia_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
    ]
