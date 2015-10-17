# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0028_auto_20151017_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speakingpresentation',
            options={'ordering': ['date']},
        ),
    ]
