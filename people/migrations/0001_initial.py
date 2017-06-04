# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buddy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=30, verbose_name='Nazwisko')),
                ('nick', models.CharField(blank=True, max_length=30, verbose_name='Ksywa')),
                ('knowage', models.TextField(verbose_name='Kilka zdań o...')),
                ('tabu', models.TextField(verbose_name='Nie rozmawiaj o...')),
            ],
        ),
    ]