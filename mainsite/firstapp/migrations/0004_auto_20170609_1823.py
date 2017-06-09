# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_article_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]