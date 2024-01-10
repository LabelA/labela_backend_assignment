import logging

from carpartsapi.exceptions.exceptions import ProductDoesNotExistException, CartDoesNotExistException, \
    OrderDoesNotExistException
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from carpartsapi.models.cart_model import Cart
from carpartsapi.models.order_model import Order
from carpartsapi.models.product_model import Product

logger = logging.getLogger(__name__)

PER_PAGE_COUNT = 10


def get_product_object(product_code):
    try:
        return Product.objects.get(product_code=product_code)
    except Product.DoesNotExist:
        message = "Product not found for the product_code : {}".format(product_code)
        logger.error(message)
        raise ProductDoesNotExistException("403", "Invalid Product id", message)


def get_cart_object(cart_id):
    try:
        return Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        message = "Cart not found for the cart id : {}".format(cart_id)
        logger.error(message)
        raise CartDoesNotExistException("403", "Invalid Cart id", message)


def get_order_object(order_id):
    try:
        return Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        message = "Order not found for the order_id : {}".format(order_id)
        logger.error(message)
        raise OrderDoesNotExistException("403", "Invalid order_id", message)


def populate_pagination(page, pagination_object):
    paginator = Paginator(pagination_object, PER_PAGE_COUNT)
    try:
        pagination_object = paginator.page(page)
    except PageNotAnInteger:
        pagination_object = paginator.page(1)
    except EmptyPage:
        pagination_object = paginator.page(paginator.num_pages)
    return pagination_object
