from rest_framework import routers
from customers.views import CustomersView

route = routers.DefaultRouter()

route.register(r"customers", CustomersView, basename="Customers")

urlpatterns = []

urlpatterns = urlpatterns + route.urls
