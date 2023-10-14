from rest_framework import viewsets

from .models import Cart
from .serializers import CartReadSerializer, CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return CartSerializer
        return CartReadSerializer
