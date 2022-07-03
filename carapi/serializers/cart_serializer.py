from statistics import mode
from rest_framework import serializers
from carapi.models.cart_model import Cart, CartItems
from carapi.models.products_model import Products
from carapi.serializers.product_serializer import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItems
        exclude = ["cart"]


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"
