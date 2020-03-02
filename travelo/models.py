from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=2083)
    des = models.TextField()
    price =models.IntegerField()
    offer=models.BooleanField(default=False)