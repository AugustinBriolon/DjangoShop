from django.db import models

class Product(models.Model):
  image = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  quantity = models.IntegerField()
  price = models.IntegerField()
