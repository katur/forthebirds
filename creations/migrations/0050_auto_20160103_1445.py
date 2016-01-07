# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0049_radioprogram_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='slug',
        ),
    ]
