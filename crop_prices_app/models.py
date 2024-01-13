# crop_prices_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Price(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
