from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductReviewViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'reviews', ProductReviewViewSet, basename='review')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
]