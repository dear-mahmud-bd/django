from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . import permissions

# Create your views here.
from rest_framework import viewsets
from . import serializers, models

class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer