# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0022_auto_20150125_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abafieldguideimage',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='abafieldguideimage',
            name='filename',
        ),
        migrations.AddField(
            model_name='abafieldguideimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'abafieldguide', blank=True),
            preserve_default=True,
        ),
    ]
