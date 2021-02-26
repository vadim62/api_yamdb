from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

User = get_user_model()


class UsersPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_admin:
            return True
        if (request.method == 'GET'
            and view.action == 'list'
                and (request.user.is_user or request.user.is_moderator)):
            return False
        if (request.method == 'POST'
                and (request.user.is_user or request.user.is_moderator)):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        is_me = (
            request.user.username == request.parser_context.get('kwargs').get(
                'username')
        )
        if is_me and request.method in ['GET', 'PATCH']:
            return True
        return False


class CategoriesGenresPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method in ['POST', 'DELETE'] and (
                request.auth is not None and request.user.is_admin):
            return True
        if request.method == 'PATCH':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return False


class CommentPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET' or (
            request.user
            and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user and request.user.is_authenticated:
            if (request.user.is_admin or request.user.is_moderator
                    or obj.author == request.user):
                return True


class ReviewPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET' or (
            request.user
            and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user and request.user.is_authenticated:
            if (request.user.is_admin or request.user.is_moderator
                    or obj.author == request.user):
                return True


class TitlesPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method in ['POST', 'DELETE', 'PATCH'] and (
                request.auth is not None and request.user.is_admin):
            return True
        return False
