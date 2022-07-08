from rest_framework import serializers


from .models import Product, Order, OrderLine

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model= Order
        fields= '__all__'

    def get_total (self, obj):
        return 0
        pass

class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderLine
        fields= '__all__'