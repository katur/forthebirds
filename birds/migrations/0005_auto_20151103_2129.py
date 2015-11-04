# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0004_auto_20151017_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='absolute_position',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Taxonomic position', blank=True),
        ),
        migrations.AlterField(
            model_name='taxonomicgroup',
            name='relative_position',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
