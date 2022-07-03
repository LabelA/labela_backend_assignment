from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True, unique=True)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True, auto_now=True)
    
    class Meta:
        db_table = "products"
        ordering = ["-created"]

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        return super(Products, self).save(*args, **kwargs)