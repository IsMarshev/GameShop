# Generated by Django 4.1.7 on 2023-04-08 10:52

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_rename_games_slider_photo_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider_photo',
            name='photo',
            field=models.ImageField(upload_to=shop.models.upload_to_path),
        ),
    ]