from django.db import models
from django.contrib.auth.models import User
from setuptools import Require


# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class NewUser(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Cart(models.Model):
    name = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    username = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
