from django.db import models
from datetime import datetime

class Buyer(models.Model):
    username = models.CharField(max_length=20)
    age = models.DateField(default=None,null=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=512)
    tel_number = models.CharField(max_length=10)
    salt = models.CharField(max_length=512, default=None)
    last_login = models.DateTimeField(auto_now=True, verbose_name='last login')
    is_authorized = models.BooleanField(default=0)
    is_superuser = models.BooleanField(default=0)


class category(models.Model):
    name_category = models.CharField(max_length=40)
    information = models.CharField(max_length=1000000)


class game(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    information = models.CharField(max_length=100000000)
    category = models.ForeignKey(
        category, on_delete=models.RESTRICT)  # Удалить CASCADE
    released = models.DateField()
    availability = models.BooleanField(default=0)

    def __str__(self):
        return self.name


def upload_to_path(instance, filename):
    return f'images/{instance.game.name}/{filename}'


class slider_photo(models.Model):
    game = models.ForeignKey(game, on_delete=models.RESTRICT)
    photo = models.ImageField(upload_to=upload_to_path)


class order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.RESTRICT)
    created = models.DateField(default=datetime.now)
    compleate = models.BooleanField(default=0)


class pre_order(models.Model):
    id_game = models.ForeignKey(game, on_delete=models.RESTRICT) 
    count = models.IntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.RESTRICT)
    order = models.ForeignKey(order, on_delete=models.RESTRICT,default=None,null=True)

# Связь от преордер к ордер, должна быть многие к одному( поменять связь)


class reviews(models.Model):
    author = models.CharField(max_length=20)
    reviews = models.CharField(max_length=1000000)
    created = models.DateField(default=datetime.now)
    game_id = models.ForeignKey(game, on_delete=models.RESTRICT)
