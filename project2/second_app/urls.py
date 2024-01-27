from django.urls import path
from . import views

urlpatterns = [
    path('cources/', views.cources),
    path('feedback/', views.feedback),
]
