# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_author_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birthday',
        ),
        migrations.AddField(
            model_name='publisher',
            name='someextra',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
