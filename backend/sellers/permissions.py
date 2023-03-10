from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read and edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user

class IsStoreOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.store.user == request.user