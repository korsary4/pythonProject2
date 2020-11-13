from django.urls import path

from .views import LoginIndexView

urlpatterns = [
   path('login/', LoginIndexView.as_view()),
  # path('', IndexView.as_view()),
]
