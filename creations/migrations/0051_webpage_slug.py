# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0050_auto_20160103_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
