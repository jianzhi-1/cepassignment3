# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='companypicture',
            field=models.ImageField(default=1, upload_to=b'company_images', blank=True),
            preserve_default=False,
        ),
    ]
