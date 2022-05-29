from django.urls import path
from .apiviews import ProductView, CartAll, ProductAdd, CartAdd, CartItem, NewUser, ProductSingleView, ProductSingleEdit

urlpatterns = [
    path('product/all', ProductView.as_view(), name='get_all_product'),
    path('product/add', ProductAdd.as_view(), name='add_product'), # This need to be admin only
    path('product/<int:pk>', ProductSingleView.as_view(), name='get_single_product'),
    path('product/modify/<int:pk>', ProductSingleEdit.as_view(),
         name='get_single_product'),
    path('cart/add', CartAdd.as_view(), name='add_product_cart'), # This need to be single user only
    path('cart/all', CartAll.as_view(), name='view_cart'), # This need to be single user only
    path('cart/<int:pk>', CartItem.as_view(), name='remove_product_cart'), 
    path('user/add', NewUser.as_view(), name='new_user'), # This need to be admin only
]