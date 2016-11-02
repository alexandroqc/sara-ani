# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20161102_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='places',
        ),
        migrations.RemoveField(
            model_name='place',
            name='schedules',
        ),
        migrations.AddField(
            model_name='placeschedule',
            name='places',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Place'),
        ),
        migrations.AddField(
            model_name='placeschedule',
            name='schedules',
            field=models.ManyToManyField(blank=True, null=True, to='events.Schedule'),
        ),
        migrations.AddField(
            model_name='event',
            name='PlaceSchedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.PlaceSchedule'),
        ),
    ]
