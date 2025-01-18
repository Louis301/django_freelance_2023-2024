from django.db import models

class Profile(models.Model):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return f'ФИО: {self.fio}; email: {self.phone}'

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    img_ref = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    profile_id = models.IntegerField(default=0)
    in_cart = models.BooleanField(default=False)
    def __str__(self):
        return f'Наименование: {self.title}'