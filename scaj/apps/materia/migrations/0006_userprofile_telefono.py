# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0005_auto_20170928_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='telefono',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
