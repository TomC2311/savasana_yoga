# Generated by Django 3.2.5 on 2021-08-26 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_class_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='evening_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='morning_time',
        ),
        migrations.AlterField(
            model_name='product',
            name='class_time',
            field=models.TimeField(default=datetime.time(10, 0)),
        ),
    ]
