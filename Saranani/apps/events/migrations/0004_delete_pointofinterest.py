# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_pointofinterest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PointOfInterest',
        ),
    ]
