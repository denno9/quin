# Generated by Django 3.0.2 on 2020-08-15 08:40

from django.db import migrations, models
import theTeam.models


class Migration(migrations.Migration):

    dependencies = [
        ('theTeam', '0004_auto_20200815_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='theteam',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=theTeam.models.upload_image_path),
        ),
    ]
