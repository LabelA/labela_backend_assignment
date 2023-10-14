from django.db import models

from products.models import Product


class Order(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    delivery_on = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
