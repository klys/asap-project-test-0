# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField( primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=2)),
                ('date_of_birth', models.DateField()),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
            ],
        ),
    ]
