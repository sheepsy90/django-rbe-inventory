# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-24 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oidc_provider', '0018_hybridflow_and_clientattrs'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociatedService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False, help_text=b'If the client is enabled or not.')),
                ('description', models.TextField(default=b'', help_text=b'A description of what the client does.')),
                ('logo_url', models.URLField(blank=True, help_text=b'A URL to the logo of the associated page.')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oidc_provider.Client')),
            ],
        ),
    ]
