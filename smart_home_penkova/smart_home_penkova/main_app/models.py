from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=20)
    devices_quantity = models.IntegerField(default=0)
    light = models.BooleanField(default=False)
    fan = models.BooleanField(default=False)
    heater = models.BooleanField(default=False)
    player = models.BooleanField(default=False)
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    voltage = models.IntegerField(default=0)