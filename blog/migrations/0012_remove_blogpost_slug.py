# Generated by Django 3.0.2 on 2020-08-12 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200812_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='slug',
        ),
    ]
