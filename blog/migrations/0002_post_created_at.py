# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
    ]
