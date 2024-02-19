from django.db import models


class CanvasModel(models.Model):
    title = models.CharField(max_length=50, default=None) 
    pen_color = models.CharField(max_length=10, default='black')
    pen_width = models.IntegerField(default=1)
