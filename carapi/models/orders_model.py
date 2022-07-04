from django.db import models
from django.utils import timezone

from carapi.models.cart_model import Cart


class Order(models.Model):

    ORDER_STATUS = [("CONFIRMED", "Confirmed"), ("DELIVERY", "Delivery")]

    id = models.BigAutoField(primary_key=True, unique=True)
    cart = models.OneToOneField(
        Cart, related_name="orders", null=True, on_delete=models.DO_NOTHING
    )
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default="CONFIRMED")
    delivery_info = models.DateTimeField(null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        db_table = "orders"
        ordering = ["-created"]
