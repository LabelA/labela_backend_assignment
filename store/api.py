from datetime import datetime
from itertools import product
import pytz
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from store.models import Order, OrderLine, Product
from store.serializers import OrderLineSerializer, OrderSerializer, ProductSerializer

class ProductApi(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    # Create, Delete and Direct Update options are only available to Admins
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # List and Detail view options do not have any restrictions (Done)


    # Add Inventory Quntity (Done)
    @action(detail=False, methods=['post'])
    def add_inventory_quantity(self, request, *args, **kwargs):
        # Get Request Data
        data = request.data
        if data.get('id') is not None:
            if data.get('qty_in_stock') is not None:
                product = Product.objects.get(id=data.get('id'))
                product.qty_in_stock += data.get('qty_in_stock')
                serialized_product = ProductSerializer(product)
                product.save()
                return Response(serialized_product.data)
            return Response({'message': 'Qty is required'}, status=400)    
        return Response({'message': 'Product id is required'}, status=400)


class OrderLineApi(viewsets.ModelViewSet):
    serializer_class = OrderLineSerializer
    queryset = OrderLine.objects.all()

    # All users can use the endpoints
    # Only Create Update and Delete endpoint should be available as the users will get the lines when they fetch the order
    # When creating an Orderline if there is no order present create it first and then create the line
    def create(self, request, *args, **kwargs):
        temp_request = request
        if temp_request.data.get('order') is None:
            # Create an order
            order = Order.objects.create(wanted_date= datetime.now(pytz.utc), status='Planned')
            temp_request.data['order'] = order.id
        # Check if an order line exist for the given product
        order_lines = OrderLine.objects.filter(order=temp_request.data.get('order'), product=temp_request.data.get('product'))
        if order_lines is None:
            super().create(temp_request, *args, **kwargs)
        else: 
            order_line = order_lines[0]
            order_line.quantity += temp_request.data['quantity']
            order_line.save()
        product = Product.objects.get(id=temp_request.data.get('product'))
        product.qty_in_stock -= temp_request.data['quantity']
        if product.qty_in_stock < 0:
            return Response({'message': 'Does not have enough stock'})
        product.save()
        order = Order.objects.get(id=temp_request.data.get('order'))
        return Response(OrderSerializer(order).data)

    def update(self, request, *args, **kwargs):
        # Change the quantity of the products
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        order_lines = OrderLine.objects.filter(id=self.kwargs.get('pk'))

        if len(order_lines) == 0:
            return super().destroy(request, *args, **kwargs)

        order_line = order_lines[0]
        product = Product.objects.get(id=order_line.product.id)
        product.qty_in_stock += order_line.quantity

        super().destroy(request, *args, **kwargs)
        product.save()
        # Update the quantity in stock
        order = Order.objects.get(id=order_line.order.id)
        return Response(OrderSerializer(order).data)


class OrderApi(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # Should not directly update status it should only be updated through the dedicated endpoint

