# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-14 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about_me_text',
            field=models.TextField(default=b'', max_length=3000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='invited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
