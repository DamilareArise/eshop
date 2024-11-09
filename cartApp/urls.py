from .views import allCart, addToCart, addQuantity
from django.urls import path

urlpatterns = [
    path('cart/<int:userId>/', allCart, name='cart'),
    path('add-to-cart/<int:productId>/', addToCart, name='add-to-cart'),
    path('add-quantity/<int:cartId>/', addQuantity, name='add-quantity')
]
