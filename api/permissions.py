from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

User = get_user_model()


class IsAnonymous(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous is True and request.method == 'GET':
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous is True and request.method == 'GET':
            return True


class IsAuthenticatedOrAuthor(BasePermission):

    def has_permission(self, request, view):
        if (request.user.is_authenticated
                and request.method in ['GET', 'POST', 'PATCH', 'DELETE']):
            return True

    def has_object_permission(self, request, view, obj):
        is_author = obj.author == request.user
        if is_author or request.user.is_admin or request.user.is_moderator:
            return True


class IsMe(BasePermission):

    def has_permission(self, request, view):
        if (request.user.is_authenticated
                and view.action == 'me'
                and request.method in ['GET', 'PATCH']):
            return True
        if (request.user.is_authenticated
                and request.method == 'DELETE'):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def has_object_permission(self, request, view, obj):
        if (request.user.is_authenticated
                and view.action == 'me'
                and request.method in ['GET', 'PATCH']):
            return True


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if (request.user.is_authenticated and request.user.is_admin
                and request.method in ['GET', 'POST', 'PATCH', 'DELETE']):
            return True

    def has_object_permission(self, request, view, obj):
        if (request.user.is_authenticated and request.user.is_admin
                and request.method in ['GET', 'POST', 'DELETE', 'PATCH']):
            return True
