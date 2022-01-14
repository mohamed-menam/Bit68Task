from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
