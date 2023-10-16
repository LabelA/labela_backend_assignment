from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"v1/orders", views.OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
