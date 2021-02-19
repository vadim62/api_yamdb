from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from api_yamdb.views import (
    RegisterUserView, UsersViewSet, MyTokenObtainPairView
)

v1_router = DefaultRouter()
v1_router.register(
    'auth/email',
    RegisterUserView
)
v1_router.register(
    'users',
    UsersViewSet
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
