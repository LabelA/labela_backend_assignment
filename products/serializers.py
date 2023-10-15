from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Product


class ProductSerializer(ModelSerializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = ("id", "name", "price")
