# Generated by Django 3.1.4 on 2020-12-23 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0004_auto_20201223_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='employe_categories',
            field=models.CharField(default=datetime.datetime(2020, 12, 23, 8, 26, 53, 84328, tzinfo=utc), max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default=datetime.datetime(2020, 12, 23, 8, 28, 43, 115982, tzinfo=utc), max_length=6),
            preserve_default=False,
        ),
    ]