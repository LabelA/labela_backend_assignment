from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers, status
from orders.models import Order, Customer
from carts.models import Cart
from customers.serializers import CustomerSerializer

from rest_framework.response import Response
from carts.serializers import CartEntrySerializer


class OrderSerializer(ModelSerializer):
    order_entries = CartEntrySerializer(many=True, required=False)
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ("id", "order_entries", "customer", "delivery_date")


class OrderCreateSerializer(Serializer):
    cart_id = serializers.IntegerField()
    delivery_date = serializers.DateTimeField()

    def validate(self, attrs):
        try:
            cart_id = attrs.get("cart_id")
            cart = Cart.objects.get(pk=cart_id)
            cust = cart.customer

            attrs["cart"] = cart
            attrs["customer"] = cust
            return attrs
        except Cart.DoesNotExist:
            return Response("Cart not Valid", status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response("Customer not Valid", status=status.HTTP_400_BAD_REQUEST)
