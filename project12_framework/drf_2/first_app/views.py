from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from . import serializers, models
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import paginations



class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AdminOrReadOnly]
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    
    # # Searching 
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'description']
    
    # # ordering with ascending or descending
    # filter_backends = [filters.OrderingFilter] # do not allow when cursor-pagination
    # ordering_fields = ['price'] # do not allow when cursor-pagination
    
    # pagination_class = paginations.ProductPagination
    # pagination_class = paginations.ProductLimitOffsetPagination
    pagination_class = paginations.ProductCursorPagination
    
    
    
    # # filtering with query parameter
    # def get_queryset(self):
    #     queryset = models.Product.objects.all()
    #     name = self.request.query_params.get('name')
    #     if name is not None:
    #         # queryset = queryset.filter(name=name)
    #         queryset = queryset.filter(name__icontains=name) # capital or small letter doesn't effect
    #     return queryset
        
    
    
    # permission_classes = [IsAuthenticated]
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
    
    # django-filtering
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user__username']
    filterset_fields = ['rating', 'product']
    
    # # Filtering against query parameters
    # def get_queryset(self):
    #     queryset = models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username) 
    #     return queryset
    