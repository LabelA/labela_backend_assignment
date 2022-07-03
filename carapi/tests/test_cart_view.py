import json
import pytest
from carapi.models.cart_model import Cart, CartItems
from carapi.models.products_model import Products
from carapi.serializers.cart_serializer import CartSerializer


QUANTITY = 2
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


@pytest.mark.django_db
class TestCart:
    def test_client_can_add_to_cart(self, client):
        product = createProduct()

        response = client().post(
            f"/cart",
            data=[{"id": product.product_id, "quantity": QUANTITY}],
            format="json",
        )

        data = json.loads(response.content)["data"]
        assert response.status_code == 201
        assert len(data["cart_items"]) == 1
        cart_items = data["cart_items"][0]
        assert int(cart_items["quantity"]) == QUANTITY
        assert cart_items["product"]["product_id"] == product.product_id
        assert cart_items["product"]["product_name"] == product.product_name
        assert int(cart_items["product"]["quantity"]) == product.quantity

    def test_client_can_remove_from_cart(self, client):
        product = createProduct()
        cart = addToCart(product.product_id)

        response = client().delete(f"/cart/{cart['cart_id']}/{product.product_id}")
        assert response.status_code == 404
