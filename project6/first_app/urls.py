from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="nav"),
    path('home/', views.home, name="home_page"),
]
