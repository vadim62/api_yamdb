from django.conf.urls import url
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from .swagger import schema_view
from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    MyTokenObtainPairView,
                    RegisterUserView,
                    ReviewViewSet, TitleViewSet, UsersViewSet)


v1_router = DefaultRouter()
v1_router.register(
    'auth/email',
    RegisterUserView
)
v1_router.register(
    'users',
    UsersViewSet
)
v1_router.register(
    'titles',
    TitleViewSet,
    basename='titles',
)
v1_router.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
v1_router.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='Review'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)

urlpatterns = [
    path(
        'auth/token/',
        MyTokenObtainPairView.as_view(),
        name='my_token_obtain_pair'
    ),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('v1/', include(v1_router.urls)),
]


urlpatterns += [
    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    url(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
