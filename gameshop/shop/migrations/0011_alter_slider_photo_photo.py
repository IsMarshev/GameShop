# Generated by Django 4.1.7 on 2023-04-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_slider_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider_photo',
            name='photo',
            field=models.ImageField(upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000001FF7906EC80>'),
        ),
    ]
