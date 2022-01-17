# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0033_remove_book_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadioProgramAirDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('program', models.ForeignKey(to='creations.RadioProgram', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
