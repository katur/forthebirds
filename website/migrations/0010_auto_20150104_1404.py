# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_userprofile_primary_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publicity_photos',
            field=models.ManyToManyField(related_name=b'uploaded_publicity_photos', to='website.UploadedImage', blank=True),
        ),
    ]
