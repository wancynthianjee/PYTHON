from django.db import models

# Create your models here.
class Product(models.model):
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    description=
