# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-26 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contact_method',
            field=models.CharField(choices=[('Email', 'Email'), ('Call', 'Call'), ('Text', 'Text')], default='Email', max_length=6),
        ),
    ]
