# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='query_body',
            field=models.TextField(blank=True, verbose_name='Query Body'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='question',
            field=models.CharField(blank=True, max_length=255, verbose_name='Question'),
        ),
    ]
