from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from carapi.models.cart_model import Cart, CartItems
from carapi.serializers.cart_serializer import CartSerializer
from carapi.models.products_model import Products
from helpers.constant import StaticResponse as info
from helpers.response import CustomResponseBuilder as rb


class CartPostView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.create()

        for item in request.data:
            product = Products.objects.get(product_id=item["id"])
            CartItems.objects.create(
                cart=cart, product=product, quantity=item["quantity"]
            )

        cart_items = CartSerializer(instance=cart)
        data = rb.getSuccessResponse(cart_items.data, info.CART_CREATED)
        return Response(data, status=status.HTTP_201_CREATED)


class CartRetrieveView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        try:
            queryset = Cart.objects.get(cart_id=kwargs["cart_id"])
            cart = CartSerializer(queryset)
            return Response(cart.data, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            data = rb.getErrorResponse({}, info.CART_NOT_FOUND)
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class CartDestroyView(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        try:
            cart_item = CartItems.objects.filter(
                cart=kwargs["cart_id"], id=kwargs["item_id"]
            )

            if cart_item.exists():
                cart_item.delete()

            # check if the cart items is empty
            # if empty, then delete cart in the exception
            CartItems.objects.get(cart=kwargs["cart_id"], id=kwargs["item_id"])
            queryset = Cart.objects.get(cart_id=kwargs["cart_id"])
            cart = CartSerializer(queryset)
            return Response(cart.data, status=status.HTTP_200_OK)

        except CartItems.DoesNotExist:
            Cart.objects.filter(cart_id=kwargs["cart_id"]).delete()
            data = rb.getValidationErrorResponse(info.CART_IS_EMPTY)
            return Response(data, status=status.HTTP_404_NOT_FOUND)
