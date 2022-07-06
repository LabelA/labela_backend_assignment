from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=150)
    total_payment = models.IntegerField()
    delivery_date = models.DateField(blank=True, null=True)
    delivery_time = models.TimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.customer
