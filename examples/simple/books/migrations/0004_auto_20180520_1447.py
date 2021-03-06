# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 19:47
from __future__ import unicode_literals

import books.models.book
from django.db import migrations
import strawberry.fields.md5


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180520_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='synopsis_hash',
            field=strawberry.fields.md5.MD5Field(always_update=True, editable=False, populate_from=books.models.book.strip_synopsis),
        ),
    ]
