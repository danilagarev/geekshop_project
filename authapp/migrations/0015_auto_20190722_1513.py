# Generated by Django 2.2.3 on 2019-07-22 10:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_auto_20190721_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 10, 13, 51, 623677, tzinfo=utc)),
        ),
    ]