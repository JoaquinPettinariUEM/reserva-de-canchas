from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsClubOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_club_owner

class IsPlayerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and request.user.is_club_owner == (not True)

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return obj.id == request.user.id

class IsCourtOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and obj.owner == request.user

class CanCreateCourt(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and request.user.is_club_owner

class ReadOnlyOrClubAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated and
            request.user.is_superuser or request.user.is_club_owner
        )
