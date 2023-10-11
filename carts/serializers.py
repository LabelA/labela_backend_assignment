from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from carts.models import Cart
from products.serializers import ProductSerializer

class CartSerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    items= ProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = (
            'id',
            'items'
        )
