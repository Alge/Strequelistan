# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-20 11:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strecklista', '0002_product_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Product categories'},
        ),
    ]