# Generated by Django 4.0.3 on 2023-10-15 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0001_initial"),
        ("carts", "0002_alter_cart_customer_delete_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer_cart",
                to="customers.customer",
            ),
        ),
    ]
