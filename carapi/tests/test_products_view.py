import json
from math import prod
import pytest
from carapi.models.products_model import Products


DATA = {"product_name": "Body Paint", "price": "299.34", "quantity": 10}


def createProduct():
    product = Products(**DATA)
    product.save()

    return product


@pytest.mark.django_db
class TestProducts:
    def test_company_can_create_products(self, client):
        response = client().post("/product", data=DATA, format="json")

        respone = json.loads(response.content)["data"]
        assert response.status_code == 201
        assert respone["product_name"] == DATA["product_name"]
        assert respone["price"] == DATA["price"]
        quantity = DATA["quantity"]
        assert respone["quantity"] == f"{quantity}"

    def test_company_can_view_all_products(self, client):
        product = createProduct()

        response = client().get("/product")
        data = json.loads(response.content)["data"]

        assert response.status_code == 200
        assert type(data) is list
        assert len(data) > 0
        assert data[0]["product_id"] == product.product_id
        assert data[0]["product_name"] == product.product_name
        assert data[0]["price"] == float(product.price)
        assert data[0]["quantity"] == f"{product.quantity}"

    def test_company_can_view_product_details(self, client):
        product = createProduct()

        response = client().get(f"/product/{product.product_id}")
        data = json.loads(response.content)["data"]

        assert response.status_code == 200
        assert type(data) is dict
        assert data["product_id"] == product.product_id
        assert data["product_name"] == product.product_name
        assert data["price"] == float(product.price)
        assert data["quantity"] == f"{product.quantity}"
