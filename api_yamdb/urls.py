from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from api_yamdb.views import CategoriesViewSet, GenresViewSet, TitlesViewSet

v1_router = DefaultRouter()
v1_router.register(
    'titles',
    TitlesViewSet,
    basename='titles'
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




urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
urlpatterns += [
    path('api/v1/', include(v1_router.urls)),
]
