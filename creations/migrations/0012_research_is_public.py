# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0011_auto_20140912_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='is_public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
