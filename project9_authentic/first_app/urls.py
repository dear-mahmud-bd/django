from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('signup/', views.signup, name='signup_page'),
    path('signin/', views.signin, name='signin_page'),
    path('profile/', views.profile, name='profile_page'),
    path('user_logout/', views.user_logout, name='logout_page'),
    path('pass_change/', views.pass_change, name='pass_change_page'),
    path('pass_change_without/', views.pass_change_without, name='pass_change_without_page'),
]
