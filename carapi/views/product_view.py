from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from carapi.serializers.product_serializer import ProductSerializer
from carapi.models.products_model import Products
from helpers.constant import StaticResponse as info
from helpers.response import CustomResponseBuilder as rb

class ProductPostGetView(ListCreateAPIView):

    def post(self, request, *args, **kwargs):
        product = ProductSerializer(data=request.data)

        if product.is_valid():
            if not product.save():
                data = rb.getValidationErrorResponse(product.errors)
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            data = rb.getSuccessResponse(product.data, info.PRODUCT_CREATED)
            return Response(data, status=status.HTTP_201_CREATED)

        data = rb.getValidationErrorResponse(product.errors)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):
        queryset = Products.objects.values()

        data = rb.getSuccessResponse(queryset, info.PRODUCT_READ)
        return Response(data, status=status.HTTP_200_OK)


class ProductGetPutDeleteView(RetrieveUpdateDestroyAPIView):

    def get(self, request, *args, **kwargs):
        queryset = Products.objects.filter(product_id=kwargs["product_id"])
        
        if not queryset.exists():
            data = rb.getErrorResponse({}, info.PRODUCT_NOT_FOUND)
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        data = queryset.values().first()
        response = rb.getSuccessResponse(data, info.PRODUCT_READ)
        return Response(response, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        queryset = Products.objects.filter(product_id=kwargs["product_id"])

        if not queryset.exists():
            data = rb.getSuccessResponse({}, info.PRODUCT_NOT_FOUND)
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        product = ProductSerializer(instance=queryset.first(), data=request.data)

        if product.is_valid():
            if not product.save():
                data = rb.getValidationErrorResponse(product.errors)
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            data = rb.getSuccessResponse(product.data, info.PRODUCT_UPDATED)
            return Response(data, status=status.HTTP_200_OK)

        data = rb.getValidationErrorResponse(product.errors)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        queryset = Products.objects.filter(product_id=kwargs["product_id"])

        if not queryset.exists():
            data = rb.getErrorResponse({}, info.PRODUCT_NOT_FOUND)
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        queryset.delete()
        data = rb.getSuccessResponse({}, info.PRODUCT_DELETED)
        return Response(data, status=status.HTTP_204_NO_CONTENT)