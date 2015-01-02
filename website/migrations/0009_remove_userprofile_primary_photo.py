# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20150101_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='primary_photo',
        ),
    ]
