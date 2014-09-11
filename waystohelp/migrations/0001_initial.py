# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WayToHelp',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'ways to help',
            },
            bases=(models.Model,),
        ),
    ]
