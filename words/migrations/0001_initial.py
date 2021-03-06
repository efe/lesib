# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sentences', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='Word')),
                ('stem', models.CharField(max_length=255, verbose_name='Stem')),
                ('content_type', models.CharField(max_length=255, verbose_name='Type of the word')),
                ('stem_type', models.CharField(max_length=255, verbose_name='Type of the stem')),
                ('morphology', models.CharField(max_length=255, verbose_name='Morphology')),
                ('position', models.PositiveSmallIntegerField(verbose_name='Postion in the parent sentence')),
                ('numbering', models.PositiveSmallIntegerField()),
                ('tag', models.CharField(max_length=255)),
                ('parent_sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='sentences.Sentence')),
            ],
        ),
    ]
