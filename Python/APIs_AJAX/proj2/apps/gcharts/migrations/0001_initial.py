# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mushrooms', models.CharField(max_length=255)),
                ('onions', models.CharField(max_length=255)),
                ('olives', models.CharField(max_length=255)),
                ('zucchini', models.CharField(max_length=255)),
                ('pepperoni', models.CharField(max_length=255)),
            ],
        ),
    ]
