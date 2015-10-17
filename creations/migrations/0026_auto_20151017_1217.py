# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0025_auto_20150726_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioprogram',
            name='supplemental_content_url',
            field=models.URLField(blank=True),
        ),
    ]
