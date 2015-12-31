# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0047_auto_20151103_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radioprogram',
            options={'ordering': ['-air_date']},
        ),
        migrations.AlterModelOptions(
            name='radioprogramrerun',
            options={'ordering': ['-air_date']},
        ),
        migrations.RenameField(
            model_name='radioprogram',
            old_name='original_air_date',
            new_name='air_date',
        ),
        migrations.RenameField(
            model_name='radioprogramrerun',
            old_name='date',
            new_name='air_date',
        ),
    ]
