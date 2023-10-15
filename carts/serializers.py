from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from carts.models import Cart, CartEntry
from products.serializers import ProductSerializer


class CartEntrySerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    product = ProductSerializer()

    class Meta:
        model = CartEntry
        fields = ("id", "product", "quantity")

class CartSerializer(ModelSerializer):
    cart_entry = CartEntrySerializer(many=True)

    class Meta:
        model = Cart
        fields = ("id", "cart_entry")
