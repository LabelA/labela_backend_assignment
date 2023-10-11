from django.db import models
from products.models import Product

# Create your models here.


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.ManyToManyField(Product, related_name="cart_product")
