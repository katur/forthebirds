# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_uploadedimage_attribution'),
        ('creations', '0031_auto_20151017_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_photo',
            field=models.ForeignKey(blank=True, to='website.UploadedImage', null=True),
        ),
    ]
