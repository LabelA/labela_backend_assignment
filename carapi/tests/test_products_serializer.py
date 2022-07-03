from typing import Dict
import pytest
from carapi.serializers.product_serializer import ProductSerializer

DATA = {"product_name": "Body Paint", "price": "299.34", "quantity": 10}


@pytest.mark.django_db
def test_product_serializer_validates_data():
    queryset = ProductSerializer(data=DATA)

    assert queryset.is_valid()
    assert len(queryset.errors) == 0
    assert queryset.data["product_name"] == DATA["product_name"]
    assert queryset.data["price"] == DATA["price"]
    quantity = DATA["quantity"]
    assert queryset.data["quantity"] == f"{quantity}"
