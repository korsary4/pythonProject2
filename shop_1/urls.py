from django.urls import path

from .views import IndexView, ShopView, CartView, WishListView

urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('shop/<int:page>', ShopView.as_view())
]
