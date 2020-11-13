from django.urls import path

from .views import IndexView, ShopView, CartView

urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('shop/<int:page>', ShopView.as_view())
]
