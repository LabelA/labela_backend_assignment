from rest_framework import routers
from carts.views import Carts

route = routers.DefaultRouter()

route.register(
    r'carts', Carts, basename="Carts"
)

urlpatterns = [
]

urlpatterns = urlpatterns + route.urls
