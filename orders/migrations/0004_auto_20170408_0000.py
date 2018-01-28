# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 18:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercheckout',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]