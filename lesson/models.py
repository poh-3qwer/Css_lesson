from django.db import models

class Rewiev(models.Model):
    username = models.CharField(max_length=60)
    text = models.TextField()
    date = models.DateTimeField()

