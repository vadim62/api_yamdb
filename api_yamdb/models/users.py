from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    
    class PermissionChoice(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'
    
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
        choices=PermissionChoice.choices,
        default=PermissionChoice.USER,
    )
    bio = models.TextField(
        verbose_name='bio',
        blank=True,
        null=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)

    @property
    def is_user(self):
        'Returns True if user has role user.'
        if self.role == 'user':
            return True
        return False


    @property
    def is_moderator(self):
        'Returns True if user has role moderator.'
        if self.role == 'moderator':
            return True
        return False

    @property
    def is_admin(self):
        'Returns True if user has role admin.'
        if self.role == 'admin' or self.is_staff is True:
            return True
        return False
