from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination

class Products(ModelViewSet):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class = PageNumberPagination
    page_size=2
