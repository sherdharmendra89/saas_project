# permissions.py
from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.content_object.__class__.__name__ == 'Company'

class IsEmployeeUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.content_object.__class__.__name__ == 'Employee'
