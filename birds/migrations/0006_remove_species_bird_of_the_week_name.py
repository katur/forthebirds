# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0005_auto_20151103_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='bird_of_the_week_name',
        ),
    ]
