# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_owners'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owners',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='post',
            name='occupation',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
