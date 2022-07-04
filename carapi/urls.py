from django.urls import path
from carapi.views.cart_view import CartDestroyView, CartRetrieveView, CartPostView
from carapi.views.order_view import OrderPostView, OrderRetrieveUpdateView
from carapi.views.product_view import ProductPostGetView, ProductGetPutDeleteView


urlpatterns = [
    path("product", ProductPostGetView.as_view(), name="cr-product"),
    path(
        "product/<int:product_id>",
        ProductGetPutDeleteView.as_view(),
        name="rud-product",
    ),
    path("cart", CartPostView.as_view(), name="c-cart"),
    path(
        "cart/<int:cart_id>",
        CartRetrieveView.as_view(),
        name="r-cart",
    ),
    path(
        "cart/<int:cart_id>/<int:item_id>",
        CartDestroyView.as_view(),
        name="d-cart",
    ),
    path("order", OrderPostView.as_view(), name="c-order"),
    path("order/<int:order_id>", OrderRetrieveUpdateView.as_view(), name="ru-order"),
]
