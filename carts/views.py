from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from carts.models import Cart
from carts.serializers import CartSerializer
from rest_framework.pagination import PageNumberPagination
from products.models import Product
from rest_framework.decorators import action


class Carts(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = PageNumberPagination
    page_size = 2

    def partial_update(self, request, pk=None):
        try:
            cart = Cart.objects.get(pk=pk)
            id = request.data.get("id")
            product = Product.objects.get(pk=id)

            cart.items.add(product)
            cart.save()
            serialized_cart = CartSerializer(cart)
            return Response(serialized_cart.data)
        except Product.DoesNotExist:
            return Response("Product does not exist")
        except Cart.DoesNotExist:
            return Response("Cart does not exist")

    @action(detail=True, methods=["DELETE"], name="delete item")
    def delete_item(self, request, pk=None):
        try:
            cart = Cart.objects.get(pk=pk)
            id = request.data.get("id")
            product = Product.objects.get(pk=id)

            cart.items.remove(product)
            cart.save()
            serialized_cart = CartSerializer(cart)
            return Response(serialized_cart.data)
        except Product.DoesNotExist:
            return Response("Product does not exist")
        except Cart.DoesNotExist:
            return Response("Cart does not exist")
