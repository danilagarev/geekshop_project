# Generated by Django 2.2.3 on 2019-07-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='активен'),
        ),
    ]