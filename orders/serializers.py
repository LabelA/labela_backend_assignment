from rest_framework import serializers

from carts.models import Cart
from products.serializers import ProductSerializer

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "name",
            "address",
            "delivery_on",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class OrderReadSerializer(OrderSerializer):
    products = ProductSerializer(many=True, required=False)

    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields + ["products"]


class OrderWriteSerializer(OrderSerializer):
    cart_id = serializers.IntegerField()

    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields + ["cart_id"]

    def validate_cart_id(self, value):
        try:
            cart = Cart.objects.get(pk=value)
            if cart.products.count() == 0:
                raise serializers.ValidationError(
                    "Cart is empty. Please add products to the cart first."
                )
            return value
        except Cart.DoesNotExist:
            raise serializers.ValidationError("Cart does not exist.")
