from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "get_products"]
    readonly_fields = ["user"]

    def get_products(self, obj):
        return list(obj.products.all())

    get_products.short_description = "Products"


admin.site.register(Cart, CartAdmin)
