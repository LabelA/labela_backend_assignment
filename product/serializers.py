from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_code", "product_name", "unit_price", "stock", "description", "type", "company", "created",
                  "updated"]
