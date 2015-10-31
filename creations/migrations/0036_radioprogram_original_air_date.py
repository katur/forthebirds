# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0035_auto_20151031_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='radioprogram',
            name='original_air_date',
            field=models.OneToOneField(null=True, blank=True, to='creations.RadioProgramAirDate'),
        ),
    ]
