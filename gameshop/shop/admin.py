from django.contrib import admin
from . import models

admin.site.register(models.category)
admin.site.register(models.game)
admin.site.register(models.slider_photo)