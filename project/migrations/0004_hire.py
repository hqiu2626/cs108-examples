# Generated by Django 2.2.7 on 2021-04-15 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210415_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(auto_now_add=True)),
                ('time_end', models.DateTimeField(auto_now_add=True)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Chef')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Customer')),
            ],
        ),
    ]
