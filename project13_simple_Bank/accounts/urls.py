from django.urls import path
from .views import home, UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView

urlpatterns = [
    path('home/', home, name='home'),
    path('registration/', UserRegistrationView.as_view(), name='registration_page'),
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('logout/', UserLogoutView.as_view(), name='logout_page'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile_page' ),
]