# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_ticket', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]