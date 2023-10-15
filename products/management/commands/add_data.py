from typing import Any, Optional
from django.core.management.base import BaseCommand
from products.models import Product
from customers.models import Customer


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        Product.objects.bulk_create(
            [
                Product(name="Engine", price=100),
                Product(name="Door", price=40),
            ]
        )

        Customer.objects.bulk_create(
            [
                Customer(name="Sahan", address="Colombo"),
                Customer(name="Kamal", address="Kandy"),
            ]
        )

        print("Seeding successful.")
