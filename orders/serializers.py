from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from orders.models import Order
from carts.models import Cart
from products.serializers import ProductSerializer
from rest_framework.response import Response

class OrderSerializer(ModelSerializer):
    items= ProductSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = (
            'id',
            'items',
            'delivery_date'
        )

class OrderCreateSerializer(Serializer):
    cart_id = serializers.IntegerField()
    delivery_date = serializers.DateTimeField()

    def validate(self, attrs):
        try:
            cart_id = attrs.get("cart_id")
            cart = Cart.objects.get(pk=cart_id)

            attrs['cart'] = cart
            return attrs
        except Cart.DoesNotExist:
            return Response("Cart not Valid")
