# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_carts_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='tax_total',
            field=models.DecimalField(decimal_places=2, default=250.0, max_digits=50),
        ),
        migrations.AddField(
            model_name='carts',
            name='total',
            field=models.DecimalField(decimal_places=2, default=250.0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='carts',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=250.0, max_digits=50),
        ),
    ]
