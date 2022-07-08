from rest_framework import viewsets
from store.models import Order, OrderLine, Product
from store.serializers import OrderLineSerializer, OrderSerializer, ProductSerializer

class ProductApi(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    # Create, Delete and Direct Update options are only available to Admins
    # List and Detail view options do not have any restrictions

class OrderLineApi(viewsets.ModelViewSet):
    serializer_class = OrderLineSerializer
    queryset = OrderLine.objects.all()

    # All users can use the endpoints
    # Only Create Update and Delete endpoint should be available as the users will get the lines when they fetch the order


class OrderApi(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    # Should not directly update status it should only be updated through the dedicated endpoint

