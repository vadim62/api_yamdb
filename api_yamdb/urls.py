from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from api_yamdb.routers import v1_router
from api_yamdb.views import MyTokenObtainPairView, schema_view

urlpatterns = [
    path(
        'auth/token/',
        MyTokenObtainPairView.MyTokenObtainPairView.as_view(),
        name='my_token_obtain_pair'
    ),
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]

urlpatterns += [
    path('api/v1/', include(v1_router.urls)),
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
