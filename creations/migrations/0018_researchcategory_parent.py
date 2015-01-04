# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0017_externalproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchcategory',
            name='parent',
            field=models.ForeignKey(blank=True, to='creations.ResearchCategory', null=True),
            preserve_default=True,
        ),
    ]
