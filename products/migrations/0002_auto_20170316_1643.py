# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-16 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImge',
            new_name='ProductImage',
        ),
    ]