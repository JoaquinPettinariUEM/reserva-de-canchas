from rest_framework.permissions import BasePermission

class IsClubOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_club_owner

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return obj.id == request.user.id
