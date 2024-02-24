from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store_book/', views.store_book, name='book_store'),
    path('show_book/', views.show_book, name='book_show'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
]
