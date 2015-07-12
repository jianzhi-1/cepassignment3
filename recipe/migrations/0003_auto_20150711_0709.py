# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20150711_0618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='content',
            new_name='information',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='food',
            name='headshot',
            field=models.ImageField(default=1, upload_to=b'food_headshots'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='rating',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
