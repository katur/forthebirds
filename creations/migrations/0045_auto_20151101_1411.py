# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0044_auto_20151101_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadioProgramRerun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('program', models.ForeignKey(to='creations.RadioProgram')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.RemoveField(
            model_name='radioprogramairdate',
            name='program',
        ),
        migrations.DeleteModel(
            name='RadioProgramAirDate',
        ),
    ]
