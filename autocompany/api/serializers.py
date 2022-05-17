from rest_framework import serializers

from .models import Client, Order, Product, ShoppingCartItem


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "model", "brand", "price"]


class ProductRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "model", "brand", "price", "image_url", "description"]


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "first_name", "last_name", "tel_no", "name", "email"]


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ["id", "client", "product", "quantity"]


class ShoppingCartDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = [
            "id",
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["client", "address", "delivery_date"]
