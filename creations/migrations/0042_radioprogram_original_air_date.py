# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0041_auto_20151101_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='radioprogram',
            name='original_air_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
