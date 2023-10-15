from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from carts.models import Cart
from customers.models import Customer
from customers.serializers import CustomerSerializer
from rest_framework.pagination import PageNumberPagination


class CustomersView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = PageNumberPagination
    page_size = 2

    def create(self, request):
        name = request.data.get("name")
        address = request.data.get("address")

        customer = Customer.objects.create(name=name, address=address)
        cart = Cart.objects.create(customer=customer)
        customer.cart = cart
        customer.save()

        serialized_customer = CustomerSerializer(customer)
        return Response(serialized_customer.data)
