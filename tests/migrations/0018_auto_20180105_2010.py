# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0017_auto_20180105_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Question'),
        ),
    ]
