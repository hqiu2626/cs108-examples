# Generated by Django 2.2.7 on 2021-03-31 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0003_statusmessage_image_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusmessage',
            old_name='image_file',
            new_name='image',
        ),
    ]