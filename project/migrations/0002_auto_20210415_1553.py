# Generated by Django 2.2.7 on 2021-04-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('profile_image_url', models.URLField(blank=True)),
                ('price_per_day_of_service', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
