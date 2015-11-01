# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0040_auto_20151101_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radioprogram',
            options={'ordering': ['-orig_air_date__date']},
        ),
        migrations.RenameField(
            model_name='radioprogram',
            old_name='original_air_date',
            new_name='orig_air_date',
        ),
    ]
