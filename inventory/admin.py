from django.contrib import admin

# Register your models here.
from inventory.models import Brand, Product

admin.site.register(Brand)
admin.site.register(Product)
