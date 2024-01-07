from django.db import models


class Product(models.Model):
    product_code = models.CharField(max_length=180)
    product_name = models.CharField(max_length=180)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    available_stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    type = models.CharField(max_length=180)
    company = models.CharField(max_length=180)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
