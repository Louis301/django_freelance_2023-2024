from django.db import models


class Track(models.Model):
    track = models.FileField('track', upload_to='audio')


