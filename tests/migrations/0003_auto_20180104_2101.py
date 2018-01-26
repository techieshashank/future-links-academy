# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-04 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20180104_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choices',
            name='id',
        ),
        migrations.AlterField(
            model_name='choices',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tests.Question'),
        ),
    ]
