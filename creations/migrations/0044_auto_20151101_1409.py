# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0043_auto_20151101_1401'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radioprogramairdate',
            options={'ordering': ['-date']},
        ),
    ]
