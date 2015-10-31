# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0034_radioprogramairdate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radioprogram',
            options={'ordering': ['-old_air_date']},
        ),
        migrations.RenameField(
            model_name='radioprogram',
            old_name='original_air_date',
            new_name='old_air_date',
        ),
    ]
