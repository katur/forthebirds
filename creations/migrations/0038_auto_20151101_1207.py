# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0037_auto_20151031_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioprogram',
            name='original_air_date',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='creations.RadioProgramAirDate'),
        ),
    ]
