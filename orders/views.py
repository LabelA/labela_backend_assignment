from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from orders.models import Order
from orders.serializers import OrderSerializer, OrderCreateSerializer
from orders.models import Product
from carts.models import Cart


class Orders(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    page_size = 2
    http_methods = {
        "get": [
            "get",
            "list",
        ],  # Allow GET for both retrieve (GET) and list (GET) actions
        "post": ["create"],  # Allow POST for create action
    }

    def create(self, request, pk=None):
        try:
            serializer = OrderCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            cart = serializer.validated_data.get("cart")
            items = cart.items.all()

            order = Order.objects.create(
                delivery_date=serializer.validated_data.get("delivery_date")
            )
            order.items.add(*items)
            order.save()

            cart.items.clear()
            cart.save()

            serialized_order = OrderSerializer(order)
            return Response(serialized_order.data)
        except Cart.DoesNotExist:
            return Response("Cart does not exist")
        except Product.DoesNotExist:
            return Response("Product does not exist")
