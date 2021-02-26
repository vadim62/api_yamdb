from .CatViewSet import CategoriesViewSet
from .CommentViewSet import CommentViewSet
from .GenresViewSet import GenresViewSet
from .RegisterUserView import RegisterUserView
from .ReviewViewSet import ReviewViewSet
from .TtilesViewSet import TitlesViewSet
from .UsersViewSet import UsersViewSet
from .swagger import schema_view, info

__all__ = [
    'CategoriesViewSet',
    'CommentViewSet',
    'GenresViewSet',
    'RegisterUserView',
    'ReviewViewSet',
    'TitlesViewSet',
    'UsersViewSet',
    'schema_view',
    'info',
]
