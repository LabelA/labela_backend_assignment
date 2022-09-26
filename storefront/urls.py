from django.urls import path, include
from rest_framework_nested import routers

from storefront import views

router = routers.SimpleRouter()
router.register('cart', views.CartViewSet, basename='cart')
router.register('orders', views.OrderView, basename='order')

entry_router = routers.NestedSimpleRouter(router, 'cart', lookup='cart')
entry_router.register('entries', views.CartEntryViewSet, basename='cart-entry')

urlpatterns = [path('', include(router.urls)), path('', include(entry_router.urls))]
