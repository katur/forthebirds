# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0007_auto_20160110_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='species',
            old_name='name',
            new_name='scientific_name',
        ),
    ]
