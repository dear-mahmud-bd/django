from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # get
            return True
        else: # put, delete, post
            return bool(request.user and request.user.is_staff)


class ReviewerOrReadOnly(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
