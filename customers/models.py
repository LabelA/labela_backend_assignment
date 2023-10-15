from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cart = models.OneToOneField(
        "carts.Cart", on_delete=models.CASCADE, null=True, related_name="customer"
    )
