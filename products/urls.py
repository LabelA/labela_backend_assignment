from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"v1/products", views.ProductViewSet, basename="Products")

urlpatterns = [
    path("", include(router.urls)),
]
