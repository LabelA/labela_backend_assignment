from django.contrib import admin
from .models import Products, Cart, NewUser

# Register your models here.
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(NewUser)
