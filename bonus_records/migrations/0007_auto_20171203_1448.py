# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 14:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bonus_records', '0006_auto_20171203_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bonus_records', to=settings.AUTH_USER_MODEL),
        ),
    ]
