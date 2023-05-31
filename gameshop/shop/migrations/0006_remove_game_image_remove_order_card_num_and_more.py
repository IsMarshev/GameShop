# Generated by Django 4.1.7 on 2023-04-08 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_game_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='image',
        ),
        migrations.RemoveField(
            model_name='order',
            name='card_num',
        ),
        migrations.RemoveField(
            model_name='order',
            name='num_order',
        ),
        migrations.AddField(
            model_name='pre_order',
            name='order',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.RESTRICT, to='shop.order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='pre_order',
            name='id_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shop.game'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='game_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shop.pre_order'),
        ),
        migrations.AlterField(
            model_name='slider_photo',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shop.game'),
        ),
        migrations.AlterField(
            model_name='slider_photo',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.DeleteModel(
            name='payment_card',
        ),
    ]
