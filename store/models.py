from django.db import models
from datetime import datetime  

from .enums import OrderStatus
class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=2, null=False, blank=False)
    qty_in_stcok = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'

class Order(models.Model):
    # products = models.ManyToManyField(Product, through='shopping_cart')
    wanted_date = models.DateTimeField(default=datetime.now ,null=False, blank=False)
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PLANNED)
    #total # Should be a derived field, Make the change in the serializer

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'order'

class OrderLines(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False, blank=False)


