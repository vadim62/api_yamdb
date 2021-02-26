from .categories_serial import CategoriesSerializer
from .comment_serial import CommentSerializer
from .genres_serial import GenresSerializer
from .register_serial import RegisterSerializer
from .review_serial import ReviewSerializer
from .titles_serial import TitleReadSerializer, TitlesSerializer
from .token_serial import MyTokenObtainPairSerializer
from .users_serial import UsersSerializer

__all__ = [
    'CategoriesSerializer',
    'CommentSerializer',
    'GenresSerializer',
    'RegisterSerializer',
    'ReviewSerializer',
    'TitleReadSerializer',
    'TitlesSerializer',
    'MyTokenObtainPairSerializer',
    'UsersSerializer',
]
