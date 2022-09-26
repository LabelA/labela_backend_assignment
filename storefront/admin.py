from django.contrib import admin

from storefront.models import Address, Order, OrderItem, Cart, CartEntry

# Register your models here.

admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartEntry)
