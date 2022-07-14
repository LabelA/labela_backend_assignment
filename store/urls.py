from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.api import OrderApi, OrderLineApi, ProductApi

router = DefaultRouter()
router.register('product', ProductApi)
router.register('order', OrderApi)
router.register('line', OrderLineApi)

urlpatterns = [
    path('', include(router.urls))
]