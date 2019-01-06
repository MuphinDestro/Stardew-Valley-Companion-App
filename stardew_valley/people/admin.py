from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Villager)
admin.site.register(models.HeartEvent)
admin.site.register(models.Item)
