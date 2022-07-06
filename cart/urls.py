from django.urls import path
from . import views
from .views import CartListApiView, CartDetailApiView


urlpatterns = [
    path('api', CartListApiView.as_view()),
    path('api/<int:cart_id>/', CartDetailApiView.as_view()),
]
