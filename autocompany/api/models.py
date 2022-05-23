from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    image_url = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tel_no = models.CharField(max_length=15)
    name = models.CharField(max_length=200)
    email = models.EmailField()


class ShoppingCartItem(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.TextField()
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
