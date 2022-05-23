from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Order, OrderItem, Product, ShoppingCartItem
from .serializers import (
    ClientSerializer,
    OrderSerializer,
    ProductListSerializer,
    ProductRetrieveSerializer,
    ShoppingCartDeleteSerializer,
    ShoppingCartSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """

    queryset = Product.objects.all()
    serializer_classes = {
        "list": ProductListSerializer,
    }
    default_serializer_class = ProductRetrieveSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, name="Get Shopping Cart")
    def cart(self, request, pk=None):
        """Retrieve the shopping cart for the client."""
        client = self.get_object()
        shopping_cart_items = ShoppingCartItem.objects.filter(client=client)
        serializer = ShoppingCartSerializer(shopping_cart_items, many=True)
        return Response(serializer.data)

    @cart.mapping.post
    def add_to_cart(self, request, pk=None):
        """Add a product to the shopping cart."""
        client = self.get_object()
        request.data["client"] = client.id
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            shopping_cart_item = ShoppingCartItem.objects.create(**serializer.validated_data)
            shopping_cart_item.save()
            serializer = ShoppingCartSerializer(shopping_cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @cart.mapping.delete
    def remove_from_cart(self, request, pk=None):
        """Remove a product from the shopping cart."""
        serializer = ShoppingCartDeleteSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data is empty for some reason
            # so we have to use the data directly from the request
            # shopping_cart_item_id = serializer.validated_data["id"]
            shopping_cart_item_id = request.data["id"]
            ShoppingCartItem.objects.filter(pk=shopping_cart_item_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["post"], detail=True, name="Order Products")
    def order(self, request, pk=None):
        """Place order for products in shopping cart."""
        client = self.get_object()
        request.data["client"] = client.id
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                order = Order.objects.create(**serializer.validated_data)
                shopping_cart_items = ShoppingCartItem.objects.filter(client=client)
                assert shopping_cart_items, "No items in shopping cart."
                order_items = [
                    OrderItem(
                        order=order,
                        product=shopping_cart_item.product,
                        quantity=shopping_cart_item.quantity,
                        rate=shopping_cart_item.product.price,
                    )
                    for shopping_cart_item in shopping_cart_items
                ]
                OrderItem.objects.bulk_create(order_items)
                shopping_cart_items.delete()
                order_data = OrderSerializer(order).data
                return Response(order_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
