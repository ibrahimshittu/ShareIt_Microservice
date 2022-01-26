from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=256)
    image = models.FileField(upload_to='images')
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass
