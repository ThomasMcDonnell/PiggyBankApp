# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bonus_records', '0010_auto_20171203_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bonus_records', to=settings.AUTH_USER_MODEL),
        ),
    ]
