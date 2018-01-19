from rest_framework import permissions


class OnlyUserCanOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or (
            request.user.id == obj.user_id
        ) or request.method == 'POST' and request.user.is_authenticated()
