# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0055_auto_20160103_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='radioprogram',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='research',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='researchcategory',
            name='slug',
        ),
    ]
