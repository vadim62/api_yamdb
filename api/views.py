from api_yamdb import settings

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt.views import TokenViewBase

from .filters import TitlesFilter
from .models import Category, Genre, Review, Title
from .pagination import YamPagination
from .permissions import IsAdmin, IsAnonymous, IsAuthenticatedOrAuthor, IsMe
from .serializers import (CategorieSerializer, CommentSerializer,
                          GenreSerializer, MyTokenObtainPairSerializer,
                          RegisterSerializer, ReviewSerializer,
                          TitleReadSerializer, TitleSerializer, UserSerializer)

User = get_user_model()


class CLDMixIn(
    viewsets.GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin
):
    pass


class MyTokenObtainPairView(TokenViewBase):
    serializer_class = MyTokenObtainPairSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsMe | IsAdmin]
    lookup_field = 'username'
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)

    @action(detail=False, methods=['get', 'patch'])
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
        else:
            serializer = self.get_serializer(
                instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


class RegisterUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def send_confirmation_code(self, email, token):
        subject = 'Confirmation code'
        message = f'Confirmation code: {token}'
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [email, ])

    def perform_create(self, serializer):
        email = serializer.validated_data.get('email')
        # создаем пользователя без пароля
        user, created = User.objects.get_or_create(email=email)
        # создаем confirmation_code, он же - пароль для пользователя
        confirmation_code = default_token_generator.make_token(user)
        # устанавливаем хэш-пароль для пользователя
        user.set_password(confirmation_code)
        # сохраняем пароль пользователя
        user.save()
        # отправляем confirmation_code на почту пользователя
        self.send_confirmation_code(email, confirmation_code)


class CategoryViewSet(CLDMixIn):
    pagination_class = YamPagination
    permission_classes = [IsAnonymous | IsAdmin]
    queryset = Category.objects.all()
    serializer_class = CategorieSerializer
    filterset_fields = ['name', ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Category, slug=self.kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreViewSet(CLDMixIn):
    pagination_class = YamPagination
    permission_classes = [IsAnonymous | IsAdmin]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Genre, slug=self.kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).order_by('id')
    # если убирать от сюда сортировку, то пишет ошибку:
    # QuerySet won't use Meta.ordering in Django 3.1
    permission_classes = [IsAnonymous | IsAdmin]
    pagination_class = YamPagination
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitleReadSerializer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = YamPagination
    permission_classes = [IsAnonymous | IsAuthenticatedOrAuthor]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = YamPagination
    permission_classes = [IsAnonymous | IsAuthenticatedOrAuthor]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, title__id=title_id)
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, title__id=title_id)
        serializer.save(author=self.request.user, review=review)
