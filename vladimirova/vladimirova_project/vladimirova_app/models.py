from django.db import models


class Account(models.Model):
    mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)


class Task(models.Model):
    closed = models.BooleanField(default=False)
    deadline = models.DateField()
    body = models.CharField(max_length=150)
    parent_task = models.CharField(default='-', max_length=150)
    account_id = models.IntegerField(default=None)

    def __str__(self):
        return self.body
    
