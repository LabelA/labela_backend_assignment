from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Product


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product_data = {
            "name": "Test Product",
            "description": "Test description",
            "price": "1500.50",
        }
        self.product = Product.objects.create(**self.product_data)

    def test_product_model(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test description")
        self.assertEqual(str(product), "Test Product")


class ProductAPITest(TestCase):
    def setUp(self):
        self.product_data = {
            "name": "Test Product",
            "description": "Test description",
            "price": "1500.50",
        }
        self.product = Product.objects.create(**self.product_data)
        self.client = APIClient()

    def test_product_list_view(self):
        url = reverse("product-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
