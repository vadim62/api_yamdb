from rest_framework.routers import DefaultRouter

from api import views

v1_router = DefaultRouter()
v1_router.register(
    'auth/email',
    views.RegisterUserView
)
v1_router.register(
    'users',
    views.UsersViewSet
)
v1_router.register(
    'titles',
    views.TitleViewSet,
    basename='titles',
)
v1_router.register(
    'categories',
    views.CategoryViewSet,
    basename='categories'
)
v1_router.register(
    'genres',
    views.GenreViewSet,
    basename='genres'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='Review'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='Comment'
)
