# Generated by Django 4.0.3 on 2022-07-02 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carapi', '0005_cartitems_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
    ]
