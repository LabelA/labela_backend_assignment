from django.db import models

from common.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    title = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    images = models.JSONField(null=True, blank=True, default=list)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    def is_in_cart(self, cart, **kwargs):
        from storefront.models import CartEntry
        cart_entry = CartEntry.objects.filter(cart=cart, product=self)
        return cart_entry.first()

    def final_price(self):
        return self.discounted_price or self.price
