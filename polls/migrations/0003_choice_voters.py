# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180523_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='voters',
            field=models.IntegerField(default=0),
        ),
    ]
