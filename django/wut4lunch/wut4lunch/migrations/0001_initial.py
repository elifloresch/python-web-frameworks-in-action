# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-23 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitter', models.CharField(max_length=63)),
                ('food', models.CharField(max_length=255)),
            ],
        ),
    ]
