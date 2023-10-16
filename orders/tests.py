from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from carts.models import Cart
from products.models import Product

from .models import Order


class OrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            name="Test Product", description="Test description", price="1500.50"
        )
        self.cart = Cart.objects.create()
        self.cart.products.add(self.product)

    def test_create_order(self):
        cart_id = self.cart.id
        order_data = {
            "name": "Test Order",
            "address": "123 Test St",
            "delivery_on": "2023-10-14T12:00:00Z",
            "cart_id": cart_id,
        }
        url = reverse("order-list")
        response = self.client.post(url, order_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(self.cart.products.count(), 0)
