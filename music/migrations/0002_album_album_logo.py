# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
