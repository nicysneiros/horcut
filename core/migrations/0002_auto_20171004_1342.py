# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='communities',
            field=models.ManyToManyField(blank=True, to='core.Community'),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_user_friends_+', to='core.User'),
        ),
    ]
