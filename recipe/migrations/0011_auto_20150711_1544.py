# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_auto_20150711_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='headshot',
            field=models.ImageField(upload_to=b'media/images'),
            preserve_default=True,
        ),
    ]
