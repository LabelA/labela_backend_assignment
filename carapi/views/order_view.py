from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from carapi.models.orders_model import Order
from carapi.serializers.order_serializer import OrderSerializer
from helpers.constant import StaticResponse as info
from helpers.response import CustomResponseBuilder as rb


class OrderPostView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        order = OrderSerializer(data=request.data)

        if order.is_valid():
            if not order.save():
                data = rb.getValidationErrorResponse(order.errors)
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            data = rb.getSuccessResponse(order.data, info.ORDER_CREATED)
            return Response(data, status=status.HTTP_201_CREATED)

        data = rb.getValidationErrorResponse(order.errors)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class OrderRetrieveUpdateView(RetrieveUpdateAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Order.objects.filter(id=kwargs["order_id"])

        if not queryset.exists():
            data = rb.getErrorResponse({}, info.ORDER_NOT_FOUND)
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        data = queryset.values().first()
        response = rb.getSuccessResponse(data, info.ORDER_RETRIEVED)
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        queryset = Order.objects.filter(id=kwargs["order_id"])

        if not queryset.exists():
            data = rb.getSuccessResponse({}, info.ORDER_NOT_FOUND)
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        order = OrderSerializer(instance=queryset.first(), data=request.data)

        if order.is_valid():
            if not order.save():
                data = rb.getValidationErrorResponse(order.errors)
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            data = rb.getSuccessResponse(order.data, info.ORDER_UPDATED)
            return Response(data, status=status.HTTP_200_OK)

        data = rb.getValidationErrorResponse(order.errors)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
