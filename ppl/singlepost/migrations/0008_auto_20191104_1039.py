# Generated by Django 2.2.6 on 2019-11-04 10:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('singlepost', '0007_auto_20191104_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 4, 10, 39, 35, 826749, tzinfo=utc)),
        ),
    ]
