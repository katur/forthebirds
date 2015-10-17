# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0030_auto_20151017_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='purchase_url',
            field=models.URLField(blank=True),
        ),
    ]
