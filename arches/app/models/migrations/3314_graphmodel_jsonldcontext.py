# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-10 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '3210_card_components'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphmodel',
            name='jsonldcontext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
