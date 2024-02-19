from django.db import models


class NotePhoto(models.Model):

    title        = models.CharField('title', max_length=100)
    category     = models.CharField('category', max_length=100) 
    comment      = models.CharField('comment', max_length=1000) 
    photo        = models.CharField('photo', max_length=1000) 

    def __str__(self):
        return f"{self.title} ({self.category})"
    
