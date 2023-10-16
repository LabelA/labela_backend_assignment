from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from products.models import Product

from .models import Cart


class CartModelTest(TestCase):
    def test_cart_creation(self):
        cart = Cart.objects.create()
        # Check the user field starts with "user-".
        # This is only for testing purposes
        self.assertTrue(cart.user.startswith("user-"))
        self.assertEqual(cart.products.count(), 0)

    def test_clean_cart_method(self):
        cart = Cart.objects.create()
        product_data = {
            "name": "Test Product",
            "description": "Test description",
            "price": "1500.50",
        }
        product = Product.objects.create(**product_data)
        cart.products.add(product)

        self.assertEqual(cart.products.count(), 1)
        cart.clean_cart()
        self.assertEqual(cart.products.count(), 0)


class CartAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            name="Test Product", description="Test description", price="1500.50"
        )

    def test_create_cart(self):
        url = reverse("cart-list")
        response = self.client.post(url, {"products": []}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(), 1)
        cart = Cart.objects.first()
        self.assertEqual(cart.products.count(), 0)

    def test_add_product_to_cart(self):
        cart = Cart.objects.create()
        update_data = {"products": [self.product.id]}
        url = reverse("cart-detail", args=[cart.id])
        response = self.client.patch(url, update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cart.refresh_from_db()
        self.assertEqual(cart.products.count(), 1)
