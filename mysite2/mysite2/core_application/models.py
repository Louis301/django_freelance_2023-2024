from django.db import models

class ContactsForm(models.Model):
    fullname = models.CharField('Имя', max_length=100)
    phone_number = models.CharField('Телефон', max_length=20)
    mail = models.CharField('Почта', max_length=40)
    message = models.CharField('Комментарий', max_length=200)

    def __str__(self):
        return f'Пользователь {self.fullname}, почта {self.mail}'
    