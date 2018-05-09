# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-04 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='perm_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
