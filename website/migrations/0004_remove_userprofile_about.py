# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20141227_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='about',
        ),
    ]
