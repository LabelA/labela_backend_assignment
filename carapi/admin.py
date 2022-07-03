from django.contrib import admin
from carapi.models.products_model import Products
from carapi.models.cart_model import Cart, CartItems
from carapi.models.orders_model import Order

# Register your models here.
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Order)
