from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='nav'),
    path('home/', views.home, name='homepage'),
    path('form/', views.form, name='formpage'),
    path('djangoform/', views.DjangoForm, name='djangoformpage'),
    path('studentform/', views.StudentForm, name='studentformpage'),
    path('passform/', views.PasswordValidation, name='passformpage'),
]
