# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20161102_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeschedule',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]