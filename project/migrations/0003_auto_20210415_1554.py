# Generated by Django 2.2.7 on 2021-04-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210415_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='chef',
            name='price_per_day_of_service',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
