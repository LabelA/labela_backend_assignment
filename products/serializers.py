from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Product


class ProductSerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()

    class Meta:
        model = Product
        fields = ("id", "name")
