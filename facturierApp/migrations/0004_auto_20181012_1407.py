# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-12 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturierApp', '0003_auto_20181012_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(choices=[('Progress', 'In Progress'), ('Relance', 'A Relancer'), ('Valid', 'Valid')], default='All', max_length=20),
        ),
    ]