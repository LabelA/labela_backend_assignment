from rest_framework import serializers

from products.serializers import ProductSerializer

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "products"]
        read_only_fields = ["id", "user"]


class CartReadSerializer(CartSerializer):
    products = ProductSerializer(many=True, required=False)

    class Meta(CartSerializer.Meta):
        read_only_fields = CartSerializer.Meta.read_only_fields + ["products"]
