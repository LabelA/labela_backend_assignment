# Generated by Django 4.0.3 on 2024-01-07 02:07

import carpartsapi.models.order_model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpartsapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, null=True, validators=[carpartsapi.models.order_model.no_past]),
        ),
    ]
