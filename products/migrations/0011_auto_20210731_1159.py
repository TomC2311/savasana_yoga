# Generated by Django 3.2.5 on 2021-07-31 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='difficulty',
        ),
        migrations.DeleteModel(
            name='DifficultyLevel',
        ),
    ]
