from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.models import Cart
from cart.serializers import CartSerializer
from product.models import Product
import logging


class CartListApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user.id)
        serializer = CartSerializer(carts, many=True)
        self.logger.debug("entering to the get cart list view")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        self.logger.debug("entering to the add cart item view")
        product_code = request.data.get('product_code')
        quantity = request.data.get('quantity')
        user = request.user.id
        product_instance = self.get_object(request.data.get('product_code'))
        available_stock = product_instance.stock
        if available_stock >= quantity:
            unit_price = product_instance.unit_price
            total_cost = unit_price * request.data.get('quantity')
            product_instance.stock = product_instance.stock - request.data.get('quantity')
            product_instance.save()
            data = {
                'product_code': product_code,
                'quantity': quantity,
                'unit_price': unit_price,
                'total_cost': total_cost,
                'user': user
            }

            serializer = CartSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"response": "quantity exceeds than available stock"},
                            status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, product_code):
        try:
            return Product.objects.get(product_code=product_code)
        except Product.DoesNotExist:
            return None


class CartDetailApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, cart_id):
        try:
            return Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return None

    def get(self, request, cart_id):
        product_instance = self.get_object(cart_id)
        self.logger.debug("entering to the cart detail view")
        if not product_instance:
            return Response(
                {"response": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CartSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_product_object(self, product_code):
        try:
            return Product.objects.get(product_code=product_code)
        except Product.DoesNotExist:
            return None

    def delete(self, request, cart_id, *args, **kwargs):
        cart_instance = self.get_object(cart_id)
        self.logger.debug("entering to the delete cart item view")
        if not cart_instance:
            return Response(
                {"response": "Object with cart id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if cart_instance is not None:
            pro_code = cart_instance.product_code
            product_instance = self.get_product_object(pro_code)
            product_instance.stock = product_instance.stock + cart_instance.quantity
            product_instance.save()
        cart_instance.delete()
        return Response(
            {"response": "Object deleted!"},
            status=status.HTTP_200_OK
        )
