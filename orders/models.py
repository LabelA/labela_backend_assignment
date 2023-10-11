from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.ManyToManyField(Product, related_name='order_product')
    delivery_date = models.DateTimeField()
