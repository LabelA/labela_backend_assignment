from statistics import mode
from rest_framework import serializers
from carapi.models.products_model import Products

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Products
        fields = '__all__'