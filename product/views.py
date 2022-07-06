from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from product.serializers import ProductSerializer
import logging


class ProductListApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.logger.debug("entering to the get product list view")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.user.is_superuser:
            data = {
                'product_code': request.data.get('product_code'),
                'product_name': request.data.get('product_name'),
                'unit_price': request.data.get('unit_price'),
                'stock': request.data.get('stock'),
                'description': request.data.get('description'),
                'type': request.data.get('type'),
                'company': request.data.get('company'),
            }
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                self.logger.debug("entering to the product create view")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.logger.error("user permission denied")
            return Response(
                {"response": "Super user only can add a products"},
                status=status.HTTP_400_BAD_REQUEST
            )


class ProductDetailApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, product_code):
        try:
            return Product.objects.get(product_code=product_code)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_code):
        product_instance = self.get_object(product_code)
        self.logger.debug("entering to the get product detail view")
        if not product_instance:
            return Response(
                {"response": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, product_code):
        if request.user.is_superuser:
            self.logger.debug("entering to the product update view")
            product_instance = self.get_object(product_code)
            if not product_instance:
                return Response(
                    {"response": "Object with project id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            data = {
                'product_code': request.data.get('product_code'),
                'product_name': request.data.get('product_name'),
                'unit_price': request.data.get('unit_price'),
                'stock': request.data.get('stock'),
                'description': request.data.get('description'),
                'type': request.data.get('type'),
                'company': request.data.get('company'),
            }
            serializer = ProductSerializer(instance=product_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"response": "Super user only can modify a product details"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, product_code):
        if request.user.is_superuser:
            product_instance = self.get_object(product_code)
            self.logger.debug("entering to the product delete view")
            if not product_instance:
                return Response(
                    {"response": "Object with product id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            product_instance.delete()
            return Response(
                {"response": "Object deleted!"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"response": "Super user only can delete a product"},
                status=status.HTTP_400_BAD_REQUEST
            )
