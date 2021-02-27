from django.conf.urls import url
from django.urls import include, path
from django.views.generic import TemplateView

from .routers import v1_router
from .swagger import schema_view
from .views import MyTokenObtainPairView

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
