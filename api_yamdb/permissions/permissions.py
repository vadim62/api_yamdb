from django.contrib.auth import get_user_model

from rest_framework import exceptions
from rest_framework.permissions import BasePermission

User = get_user_model()


class UsersPermissions (BasePermission):

    def has_permission(self, request, view):
        if request.user.is_admin == True:
            return True
        if (request.method == 'GET' and 
            view.action == 'list' and 
            request.user.role in ['user', 'moderator']
            ):
            return False
        if (request.method == 'POST' and 
            request.user.role in ['user', 'moderator']
            ):
            return False
        return True
        
    def has_object_permission(self, request, view, obj):
        if request.user.is_admin == True or request.user.role == 'admin':
            return True       
        is_me = (
            request.user.pk == request.parser_context.get('kwargs').get('pk')
        )
        if is_me and request.method in ['DELETE']:
            raise exceptions.MethodNotAllowed(request.method)
        if is_me and request.method in ['GET', 'PATCH']:
            return True
        return False


class CategoriesGenresPermissions (BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET' and request.auth is None:
            return True
        if request.method in ['POST', 'DELETE'] and (
            request.auth is not None and (
            request.user.is_admin == True or 
            request.user.role == 'admin')):
            return True
        return False

        
class CommentsPermissions (BasePermission):
    pass


class ReviewsPermissions (BasePermission):
    pass


class TitlesPermissions (BasePermission):
    pass
