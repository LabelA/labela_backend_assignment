from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from carts.models import Cart, CartEntry
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
            id = request.data.get("product_id")
            product = Product.objects.get(pk=id)

            CartEntry.objects.create(
                product=product,
                quantity=request.data.get("quantity", 1),
                cart_id=cart,
            )
            serialized_cart = CartSerializer(cart)
            return Response(serialized_cart.data)
        except Product.DoesNotExist:
            return Response("Product does not exist")
        except Cart.DoesNotExist:
            return Response("Cart does not exist")

    # remove product from cart
    @action(detail=True, methods=["delete"])
    def remove_product(self, request, pk=None):
        try:
            cart = Cart.objects.get(pk=pk)
            id = request.data.get("product_id")
            product = Product.objects.get(pk=id)
            cart_entry = CartEntry.objects.get(cart_id=cart, product=product)
            cart_entry.delete()
            serialized_cart = CartSerializer(cart)
            return Response(serialized_cart.data)
        except Product.DoesNotExist:
            return Response("Product does not exist")
        except Cart.DoesNotExist:
            return Response("Cart does not exist")
        except CartEntry.DoesNotExist:
            return Response("CartEntry does not exist")
