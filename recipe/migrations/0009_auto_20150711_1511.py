# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_delete_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='headshot',
            field=models.ImageField(upload_to=b'recipe/media/images/'),
            preserve_default=True,
        ),
    ]
