# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name=b'Visible on website'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='species',
            name='absolute_position',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Taxonomic position'),
        ),
        migrations.AlterField(
            model_name='species',
            name='is_hidden',
            field=models.BooleanField(default=False, verbose_name=b'Hidden from website'),
        ),
    ]
