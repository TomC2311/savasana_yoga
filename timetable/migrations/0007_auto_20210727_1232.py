# Generated by Django 3.2.5 on 2021-07-27 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_information'),
        ('timetable', '0006_auto_20210727_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='day_name',
        ),
        migrations.AddField(
            model_name='timetable',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], default='Monday', max_length=10),
        ),
        migrations.DeleteModel(
            name='TimeTableItems',
        ),
    ]
