from django.db import models


class Dish(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=None)
    in_shopping_cart = models.BooleanField(default=False)
    category = models.CharField(max_length=200)
    photo = models.FileField('dish_photo', upload_to='image')
    for_an_order = models.BooleanField(default=False)
    in_order_list = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.title} (блюдо)'


class Category(models.Model):
    title = models.CharField(max_length=200)
    photo = models.FileField('category_photo', upload_to='image')

    def __str__(self):
        return f'{self.title} (категория)'
    