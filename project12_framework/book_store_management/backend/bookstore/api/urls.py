from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')

urlpatterns = [
    # path('books/', views.BookListView.as_view()), # wuill handle get and post requests
    # path('books/<int:pk>/', views.BookListUpdateDelete.as_view()), # update, delete
    
    # path('books/', views.BookListCreateAPIView.as_view()), # wuill handle get and post requests
    # path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()), 
    
    path('', include(router.urls))
]