import random

from django.db import models

from products.models import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        # Add a random string to the user field instead of the actual user
        # This is only for testing purposes
        self.user = "user-" + str(random.randint(1000, 9999))
        return super().save(force_insert, force_update, using, update_fields)

    def clean_cart(self):
        """Remove all products from the cart"""
        self.products.clear()
