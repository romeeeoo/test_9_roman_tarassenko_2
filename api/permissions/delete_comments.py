from rest_framework import permissions
from rest_framework.permissions import BasePermission


class DeleteCommentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.author
