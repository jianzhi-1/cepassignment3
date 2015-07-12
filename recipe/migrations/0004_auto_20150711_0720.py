# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20150711_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='headshot',
            field=models.ImageField(upload_to=b'food_headshots/'),
            preserve_default=True,
        ),
    ]
