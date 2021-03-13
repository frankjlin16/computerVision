from django.db import models


# Create your models here.
class Image(models.Model):
    """ Model for image """
    image = models.ImageField(upload_to='uploads/images/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
