from rest_framework import routers
from products.views import Products

route = routers.DefaultRouter()

# app_name = 'products'
route.register(
    r'products', Products, basename="Products"
)

urlpatterns = [

]

urlpatterns = urlpatterns + route.urls