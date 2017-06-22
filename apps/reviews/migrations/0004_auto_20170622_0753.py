# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='book_author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='book',
            new_name='review_book',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='review_user',
        ),
    ]