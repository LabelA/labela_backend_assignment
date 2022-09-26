from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from inventory import models


class BrandSerializer(ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ('name',)


class ProductSerializer(ModelSerializer):
    brand = serializers.CharField(source="brand.name", read_only=True)

    class Meta:
        model = models.Product
        fields = ('id', 'title', 'brand', 'price', 'discounted_price', 'description', 'images',)
