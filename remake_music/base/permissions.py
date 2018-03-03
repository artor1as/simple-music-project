from rest_framework import permissions


class OnlyUserCanOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            user_id = obj.user_id
        except AttributeError:
            user_id = obj.id
        return request.method in permissions.SAFE_METHODS or (
            request.user.id == user_id
        ) or request.method == 'POST' and request.user.is_authenticated()


class OnlyAnonUserCan(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_anonymous
