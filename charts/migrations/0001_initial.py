# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OKCoinSpot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_stamp', models.FloatField()),
                ('date_local', models.DateTimeField()),
                ('buy', models.FloatField()),
                ('high', models.FloatField()),
                ('last', models.FloatField()),
                ('low', models.FloatField()),
                ('sell', models.FloatField()),
                ('vol', models.FloatField()),
            ],
        ),
    ]
