# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0002_grado'),
    ]

    operations = [
        migrations.AddField(
            model_name='grado',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='materia',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
