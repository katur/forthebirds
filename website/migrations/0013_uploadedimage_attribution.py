# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_userprofile_speaking_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='attribution',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
