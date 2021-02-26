from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        unique=True,
        max_length=255,
        blank=True,
        null=True,
    )
    role = models.CharField(
        verbose_name='role',
        max_length=20,
        choices=ROLES,
        default=USER,
    )
    bio = models.TextField(
        blank=True,
        null=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email', ]
