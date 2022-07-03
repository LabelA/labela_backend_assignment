import json
from django.utils.dateparse import parse_datetime
import pytest
from carapi.models.cart_model import Cart, CartItems
from carapi.models.orders_model import Order
from carapi.models.products_model import Products
from carapi.serializers.cart_serializer import CartSerializer


QUANTITY = 2
DELIVERY_DATE = "2022-07-10 13:08:10"
PRODUCT_DATA = {"product_name": "Car Mirror Side", "price": "1299.34", "quantity": 17}


def createProduct():
    product = Products(**PRODUCT_DATA)
    product.save()

    return product


def addToCart(id):
    product = Products.objects.get(product_id=id)
    cart = Cart.objects.create()
    CartItems.objects.create(cart=cart, product=product, quantity=QUANTITY)

    cart_items = CartSerializer(instance=cart)

    return cart_items.data


def createOrder(cart_id):
    cart = Cart.objects.get(cart_id=cart_id)
    order = Order(cart=cart)
    order.save()

    return order


@pytest.mark.django_db
class TestCart:
    def test_client_can_create_order(self, client):
        product = createProduct()
        cart = addToCart(product.product_id)

        response = client().post(
            f"/order",
            data={"cart": cart["cart_id"]},
            format="json",
        )

        data = json.loads(response.content)["data"]
        assert response.status_code == 201
        assert data["status"] == "CONFIRMED"
        assert data["cart"] == cart["cart_id"]

    def test_client_can_add_shipping_info(self, client):
        product = createProduct()
        cart = addToCart(product.product_id)
        order = createOrder(cart["cart_id"])

        response = client().put(
            f"/order/{order.id}",
            data={"delivery_info": DELIVERY_DATE},
            format="json",
        )

        data = json.loads(response.content)["data"]
        assert response.status_code == 200
        formatted_datetime = parse_datetime(data["delivery_info"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        assert formatted_datetime == DELIVERY_DATE
        assert data["cart"] == cart["cart_id"]
        assert data["status"] == "CONFIRMED"
