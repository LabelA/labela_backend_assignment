from rest_framework import serializers
from django.db.models import Sum, F

from .models import Product, Order, OrderLine

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'


class OrderLineSerializer(serializers.ModelSerializer):

    total = serializers.SerializerMethodField()
    class Meta:
        model= OrderLine
        fields= '__all__'

    def get_total (self, obj):
        return obj.quantity * obj.product.price

class OrderSerializer(serializers.ModelSerializer):

    lines = OrderLineSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model= Order
        fields= '__all__'

    def get_total (self, obj):
        return obj.lines.all().aggregate(total_price = Sum(F('quantity') * F('product__price')))