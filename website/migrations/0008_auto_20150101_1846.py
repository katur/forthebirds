# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_userprofile_publicity_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='main_photo',
            field=models.ForeignKey(related_name=b'main_uploaded_photo', blank=True, to='website.UploadedImage', null=True, on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publicity_photos',
            field=models.ManyToManyField(related_name='uploaded_publicity_photos', to= 'website.UploadedImage'),
        ),
    ]
