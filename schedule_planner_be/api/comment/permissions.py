from rest_framework.permissions import BasePermission


class LocationPermissionsMixin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Super Admin'
