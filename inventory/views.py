from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

# Create your views here.
from inventory import serializers
from inventory.models import Product


class ProductView(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        brand = self.request.query_params.get('brand')
        if brand:
            qs = qs.filter(brand=brand)

        return qs
