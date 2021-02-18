from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import RegisterUserView, MyTokenObtainPairView, UsersViewSet


router = DefaultRouter()
router.register('auth/email', RegisterUserView)
router.register(r'users', UsersViewSet)


urlpatterns = [
    path('auth/token/', MyTokenObtainPairView.as_view(), name='my_token_obtain_pair'),
    path('v1/', include(router.urls))
]