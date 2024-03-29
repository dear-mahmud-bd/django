from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="homepage"),
    path('delete/<int:roll>', views.delete_student, name="delete_student"),
    path('show/', views.showData, name="showpage"),
]