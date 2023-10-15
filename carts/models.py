from django.db import models
from products.models import Product

# Create your models here.


class Cart(models.Model):
    id = models.AutoField(primary_key=True)


class CartEntry(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart_id = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_entries"
    )
    order_id = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        null=True,
        related_name="order_entries",
    )
