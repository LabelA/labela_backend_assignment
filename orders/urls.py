from rest_framework import routers
from orders.views import Orders

route = routers.DefaultRouter()

route.register(r"orders", Orders, basename="Orders")

urlpatterns = []

urlpatterns = urlpatterns + route.urls
