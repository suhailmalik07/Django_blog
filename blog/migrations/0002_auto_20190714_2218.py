# Generated by Django 2.2.3 on 2019-07-14 16:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2019, 7, 14, 16, 48, 9, 443060, tzinfo=utc)),
        ),
    ]
