from django.urls import path, include
from .views import HomePageView

urlpatterns = [
  path('', HomePageView.as_view(), name = 'home'), # (views.py) dan HomePageView chaqirildi (url)berildi
  ]