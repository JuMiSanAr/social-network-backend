from rest_framework.permissions import BasePermission


class PostPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.posted_by and obj.posted_by.user == request.user:
            return True
        elif request.method == 'GET' or request.user.is_superuser:
            return True


class CommentPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user and obj.user == request.user.profile:
            return True
        elif request.method == 'GET' or request.user.is_superuser:
            return True


class UserPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' or obj == request.user or request.user.is_superuser:
            return True


class FriendRequestPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if (obj.sent_by == request.user.profile and (request.method == 'GET' or request.method == 'DELETE')) \
                or (obj.received_by == request.user.profile and request.method != 'DELETE') \
                or request.user.is_superuser:
            return True
