from django.urls import path, include
from .views import (
    ProductListApiView, ProductDetailApiView
)

urlpatterns = [
    path('api', ProductListApiView.as_view()),
    path('api/<str:product_code>/', ProductDetailApiView.as_view()),
]