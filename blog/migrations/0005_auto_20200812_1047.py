# Generated by Django 3.0.2 on 2020-08-12 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200812_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='date1',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]