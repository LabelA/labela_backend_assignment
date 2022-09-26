from decimal import Decimal

from django.contrib.auth.models import User, AnonymousUser
from django.db import models, transaction
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from inventory.models import Product

ADDRESS_CHOICES = (('B', 'Billing'), ('S', 'Shipping'),)

ORDER_STATUS = (('OPEN', 'Open'), ('PLACED', 'Placed'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'))


class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class OrderManager(models.Manager):
    def create_from_cart(self, cart):
        order = self.model(user=cart.user)
        order.populate_from_cart(cart)
        return order


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="OPEN")
    shipping_address = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL,
                                         blank=True, null=True)
    billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL,
                                        blank=True, null=True)
    delivery_date = models.DateField(null=True, blank=True)
    delivery_time = models.TimeField(null=True, blank=True)
    extra = models.JSONField(verbose_name=_("Extra fields"),
                             help_text=_("Arbitrary information for this order object on the moment of purchase."),
                             null=True, blank=True, default=dict)
    total_amount = models.FloatField()
    currency = models.CharField(max_length=7, editable=False, help_text=_("Currency in which this order was concluded"),
                                default="$")

    objects = OrderManager()

    def __str__(self):
        return self.user.username

    @property
    def order_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.total_price
        return total

    @transaction.atomic
    def populate_from_cart(self, cart):
        for cart_item in cart.items.all():
            order_item = OrderItem(order=self)
            try:
                order_item.populate_from_cart_entry(cart_item)
                order_item.save()
                cart_item.delete()
            except OrderItem.DoesNotExist:
                pass
        self.total_amount = self.order_total
        self.save()


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey('Order', on_delete=CASCADE, related_name="items")
    unit_price = models.FloatField()
    total_price = models.FloatField()

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def populate_from_cart_entry(self, cart_item):
        if cart_item.quantity == 0:
            raise CartEntry.DoesNotExist("Cart Item is not available")
        self.product = cart_item.product
        self.unit_price = Decimal(cart_item.product.final_price())
        self.quantity = cart_item.quantity
        self.total_price = self.unit_price * self.quantity


class CartManager(models.Manager):

    def get_or_create_from_request(self, request):
        has_customer_cart = hasattr(request, '_customer_cart')
        if not request.user or isinstance(request.user, AnonymousUser):
            # TODO: Add functionality to support cart creation for logged in user
            raise self.model.DoesNotExist
        if not has_customer_cart or request._customer_cart.user.user_id != request.user.user_id:
            request._customer_cart, created = self.get_or_create(user=request.user)
        return request._customer_cart


class CartEntryManager(models.Manager):
    def get_or_create(self, **kwargs):
        cart = kwargs.pop('cart')
        product = kwargs.pop('product')
        quantity = int(kwargs.pop('quantity', 1))

        cart_entry = product.is_in_cart(cart)
        if cart_entry:
            cart_entry.quantity += quantity
            created = False
        else:
            cart_entry = self.model(cart=cart, product=product, quantity=quantity)
            created = True
        cart_entry.save()
        return cart_entry, created


class Cart(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    version = models.IntegerField(default=1)
    extra = models.JSONField(verbose_name=_("Extra information for this cart"), null=True, blank=True, default=dict)

    objects = CartManager()

    def __str__(self):
        return f"{self.user}'s cart"

    def clear(self):
        if self.id:
            self.items.all().delete()

    @property
    def total_amount(self):
        amount = 0
        for item in self.items.all():
            amount += item.product.final_price() * item.quantity
        return amount

    @property
    def total_items(self):
        return self.items.filter(quantity__gt=0).count()

    @property
    def total_quantity(self):
        return self.items.aggregate(quantity=models.Sum('quantity'))['quantity'] or 0

    @property
    def is_empty(self):
        return self.total_items == 0 and self.total_quantity == 0


class CartEntry(BaseModel):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField()

    objects = CartEntryManager()

    class Meta:
        verbose_name_plural = 'Cart Entries'

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.title)
