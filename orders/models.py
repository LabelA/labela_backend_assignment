from django.db import models
from carts.models import CartEntry
from customers.models import Customer

# Create your models here.


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
