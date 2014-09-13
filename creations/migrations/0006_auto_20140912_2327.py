# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0005_article_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation')),
                ('date', models.DateField(null=True, blank=True)),
                ('url', models.URLField(blank=True)),
                ('file', models.FileField(null=True, upload_to=b'research', blank=True)),
                ('text', models.TextField(help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': 'Research',
            },
            bases=('creations.creation',),
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_published']},
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['title']},
        ),
    ]
