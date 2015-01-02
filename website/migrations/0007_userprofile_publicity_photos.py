# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150101_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='publicity_photos',
            field=models.ManyToManyField(to='website.UploadedImage'),
            preserve_default=True,
        ),
    ]
