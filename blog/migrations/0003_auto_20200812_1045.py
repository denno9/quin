# Generated by Django 3.0.2 on 2020-08-12 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200812_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='date1',
        ),
    ]