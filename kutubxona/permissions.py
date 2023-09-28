from rest_framework.permissions import BasePermission

class StaffPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 2:
            return True
        return False
    

class AdminPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 3 or request.user.roles == 2:
            return True
        return False 
    

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.roles == 2 or request.user.roles == 3:
            return True
        return False
    
