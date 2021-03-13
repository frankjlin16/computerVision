from django.db import models


# Create your models here.
class Images(models.Model):
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
