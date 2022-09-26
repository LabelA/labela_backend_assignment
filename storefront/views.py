# Create your views here.
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from storefront import serializers
from storefront.models import Order, Cart, CartEntry, Address
from storefront.serializers import CartSerializer, CartEntrySerializer, CheckoutSerializer, OrderSerializer


class OrderPermission(BasePermission):
    """
    Allow access to a given Order if the user is entitled to.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            detail = _("Only signed in customers can view their list of orders.")
            raise PermissionDenied(detail=detail)
        return True

    def has_object_permission(self, request, view, order):
        if request.user.is_authenticated:
            return order.user.pk == request.user.pk
        detail = _("This order does not belong to you.")
        raise PermissionDenied(detail=detail)


class OrderView(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, OrderPermission]
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()


class CartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CartSerializer
    checkout_serializer = CheckoutSerializer
    order_serializer = OrderSerializer
    queryset = Cart.objects.all()
    http_method_names = ['get', 'post']

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk, **kwargs):
        cart = Cart.objects.get(id=pk)
        context = self.get_serializer_context()
        checkout_data = self.checkout_serializer(data=request.data, context=context)
        if checkout_data.is_valid():
            validated_data = checkout_data.validated_data
            print(validated_data)
            with transaction.atomic() as txn:
                shipping_address = Address(user=request.user, **validated_data["shipping_address"]).save()
                billing_address = Address(user=request.user, **validated_data["billing_address"]).save()
                order = Order.objects.create_from_cart(cart)
                order.shipping_address = shipping_address
                order.billing_address = billing_address
                order.delivery_date = validated_data["delivery_date"]
                order.delivery_time = validated_data["delivery_time"]
                order.status = "PLACED"
                order.save()
                order_response = self.order_serializer(order)
                return Response(data=order_response.data, status=status.HTTP_201_CREATED)
        return Response(checkout_data.errors)


class CartEntryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CartEntrySerializer
    queryset = CartEntry.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
