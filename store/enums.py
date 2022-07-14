from django.db import models

class OrderStatus(models.TextChoices):
    PLANNED = 'Planned'
    COMPLETED = 'Completed'