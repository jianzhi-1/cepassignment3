# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20150711_0734'),
    ]

    operations = [
        migrations.DeleteModel(
            name='region',
        ),
    ]
