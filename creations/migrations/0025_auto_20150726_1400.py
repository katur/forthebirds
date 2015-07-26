# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0024_auto_20150726_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speakingprogram',
            options={'ordering': ['title']},
        ),
    ]
