# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_uploadedimage_attribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='image_again',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=website.models.get_updated_filename, blank=True),
        ),
    ]
