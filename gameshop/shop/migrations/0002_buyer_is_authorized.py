# Generated by Django 4.1.7 on 2023-04-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='is_authorized',
            field=models.BooleanField(default=0),
        ),
    ]
