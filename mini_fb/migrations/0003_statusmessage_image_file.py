# Generated by Django 2.2.7 on 2021-03-31 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0002_statusmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
