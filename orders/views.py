from rest_framework import status, viewsets
from rest_framework.response import Response

from carts.models import Cart

from .models import Order
from .serializers import (
    OrderReadSerializer,
    OrderSerializer,
    OrderWriteSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action in ["create"]:
            return OrderWriteSerializer
        if self.action in ["update", "partial_update"]:
            return OrderSerializer
        return OrderReadSerializer

    def create(self, request, *args, **kwargs):
        """Create a new order"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the cart and the products
        cart_id = serializer.validated_data.pop("cart_id")
        cart = Cart.objects.get(pk=cart_id)
        cart_products = cart.products.all()

        # Place the order
        serializer.validated_data["products"] = cart_products
        instance = serializer.save()

        # Clean the cart
        cart.clean_cart()

        order_serializer = OrderReadSerializer(instance)
        headers = self.get_success_headers(order_serializer.data)
        return Response(
            order_serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
