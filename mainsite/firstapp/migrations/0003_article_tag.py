# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('texh', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]
