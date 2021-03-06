# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 17:23
from __future__ import unicode_literals

import bonus_records.validators
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus_records', '0009_auto_20171203_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='user',
        ),
        migrations.AlterField(
            model_name='record',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.contrib.auth.models.User, related_name='bonus_records', to='companies.Company', validators=[bonus_records.validators.company_user_validation]),
        ),
    ]
