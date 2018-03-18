# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-10 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.AddField(
            model_name='profile',
            name='productm2m',
            field=models.ManyToManyField(to='signup.Product'),
        ),
    ]
