from django.db import models

# Create your models here.
class Problem(models.Model):
    wording = models.CharField('формулировка', max_length=100)