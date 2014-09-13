# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0008_researchcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='category',
            field=models.ForeignKey(default=1, to='creations.ResearchCategory'),
            preserve_default=False,
        ),
    ]
