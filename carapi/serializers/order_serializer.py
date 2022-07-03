from statistics import mode
from rest_framework import serializers
from carapi.models.orders_model import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
