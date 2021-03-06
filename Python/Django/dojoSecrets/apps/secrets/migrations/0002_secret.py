# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like', models.ManyToManyField(related_name='liked', to='secrets.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secrets', to='secrets.User')),
            ],
            managers=[
                ('secretMan', django.db.models.manager.Manager()),
            ],
        ),
    ]
