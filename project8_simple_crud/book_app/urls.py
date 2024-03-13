from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:roll>/', views.MyTemplateView.as_view(), {'author':'Ami'}, name='home'),
    # path('home/', views.TemplateView.as_view(template_name='home.html'), name='t_home'),
    path('home/', views.MyTemplateView.as_view(template_name='home.html'), name='t_home'),
    
    
    # path('store_book/', views.store_book, name='book_store'),
    path('store_book/', views.BookFormView.as_view(), name='book_store'),
    
    
    # path('show_book/', views.show_book, name='book_show'),
    path('show_book/', views.BookStoreModelListView.as_view(), name='book_show'),
    path('details_book/<int:id>', views.BookStoreModelDetailView.as_view(), name='book_details'),
    
    
    # path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('edit_book/<int:pk>', views.BookUpdateView.as_view(), name='edit_book'),
    
    
    # path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('delete_book/<int:pk>', views.DeleteBookView.as_view(), name='delete_book'),
]
