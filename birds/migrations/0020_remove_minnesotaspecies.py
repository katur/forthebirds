# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0019_auto_20160211_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minnesotaspecies',
            name='species',
        ),
        migrations.DeleteModel(
            name='MinnesotaSpecies',
        ),
    ]
