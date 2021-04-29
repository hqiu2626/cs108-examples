# Generated by Django 2.2.7 on 2021-04-24 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_customer_profile_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('5', 5), ('4', 4), ('3', 3), ('2', 2), ('1', 1)], max_length=1, null=True),
        ),
    ]
