# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0036_radioprogram_original_air_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radioprogram',
            options={'ordering': ['-original_air_date__date']},
        ),
        migrations.RemoveField(
            model_name='radioprogram',
            name='old_air_date',
        ),
    ]
