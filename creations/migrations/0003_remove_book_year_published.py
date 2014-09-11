# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0002_auto_20140911_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='year_published',
        ),
    ]
