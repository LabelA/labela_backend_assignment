from django.db import models
from django.utils import timezone
from carapi.models.products_model import Products


class Cart(models.Model):
    cart_id = models.BigAutoField(primary_key=True, unique=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        db_table = "cart"
        ordering = ["-created"]


class CartItems(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Products, related_name="cart_items", on_delete=models.CASCADE
    )
    quantity = models.CharField(max_length=255, default=1)

    class Meta:
        db_table = "cart_items"
