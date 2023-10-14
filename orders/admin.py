from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "delivery_on"]


admin.site.register(Order, OrderAdmin)
