# Generated by Django 4.1.7 on 2023-04-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_game_image_remove_order_card_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider_photo',
            name='photo',
            field=models.ImageField(upload_to='images/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]
