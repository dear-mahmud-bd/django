from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='nav'),
    path('home/', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('subjects/', views.subjects, name='subjectspage'),
]
