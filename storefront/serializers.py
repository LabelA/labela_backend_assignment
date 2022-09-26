from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer

from inventory.serializers import ProductSerializer
from storefront import models
from storefront.models import CartEntry, Cart


class AddressSerializer(ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'
        read_only_fields = ('id', 'user',)


class OrderItemSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = models.OrderItem
        fields = ('id', 'product', 'quantity', 'unit_price', 'total_price',)


class CheckoutSerializer(serializers.Serializer):
    shipping_address = AddressSerializer()
    billing_address = AddressSerializer()
    delivery_date = serializers.DateField()
    delivery_time = serializers.TimeField()

    class Meta:
        fields = ('shipping_address', 'billing_address', 'delivery_date', 'delivery_time')


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)
    shipping_address = AddressSerializer()
    billing_address = AddressSerializer()

    class Meta:
        model = models.Order
        fields = (
            'id', 'user', 'status', 'items', 'shipping_address', 'billing_address', 'ordered_date', 'delivery_date',
            'delivery_time', 'total_amount')


class CartEntrySerializer(ModelSerializer):
    class Meta:
        model = models.CartEntry
        fields = ('id', 'product', 'quantity',)
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        try:
            validated_data['cart'] = Cart.objects.get_or_create_from_request(self.context['request'])
        except Cart.DoesNotExist:
            raise AssertionError("Couldn't find cart to add items")

        cart_item, _ = CartEntry.objects.get_or_create(**validated_data)
        return cart_item

    def validate_product(self, product):
        if not product.is_active:
            msg = "Product `{}` is inactive, and can not be added to the cart."
            raise serializers.ValidationError(msg.format(product))
        return product


class CartSerializer(ModelSerializer):
    items = CartEntrySerializer(many=True, read_only=True)
    total_quantity = serializers.IntegerField(read_only=True)
    total_items = serializers.IntegerField(read_only=True)
    total_amount = serializers.FloatField(read_only=True)

    class Meta:
        model = models.Cart
        fields = ('id', 'items', 'total_quantity', 'total_items', 'total_amount')

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user") and not isinstance(request.user, AnonymousUser):
            user = request.user
        else:
            raise exceptions.AuthenticationFailed("You're not authorized to add items to cart. Please log in.")
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart
