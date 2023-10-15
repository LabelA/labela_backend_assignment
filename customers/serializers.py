from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(ModelSerializer):
    name = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Customer
        fields = ("id","name", "address", "cart")
