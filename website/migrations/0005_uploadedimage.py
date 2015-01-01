# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_userprofile_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_uploaded', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('image', models.ImageField(upload_to=website.models.get_updated_filename)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
