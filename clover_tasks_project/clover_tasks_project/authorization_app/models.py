from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField('логин', max_length=100)