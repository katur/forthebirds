# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0007_research_attribution'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
