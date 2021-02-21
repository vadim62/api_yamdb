from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from api_yamdb.views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                             MyTokenObtainPairView, RegisterUserView,
                             ReviewViewSet, TitlesViewSet, UsersViewSet)

v1_router = DefaultRouter()
v1_router.register(
    'auth/email',
    RegisterUserView
)
v1_router.register(
    r'users',
    UsersViewSet
)
v1_router.register(
    'titles',
    TitlesViewSet,
    basename='titles',
)
v1_router.register(
    'categories',
    CategoriesViewSet,
    basename='categories'
)
v1_router.register(
    'genres',
    GenresViewSet,
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
        MyTokenObtainPairView.MyTokenObtainPairView.as_view(),
        name='my_token_obtain_pair'
    ),
    path(
        'admin/',
        admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
urlpatterns += [
    path('api/v1/', include(v1_router.urls)),
]

schema_view = get_schema_view(
   openapi.Info(
      title="YamDB API",
      default_version='v1',
      description="API schema for YamDB project",
      terms_of_service="*",
   ),
   public=True,
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]