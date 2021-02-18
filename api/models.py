from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if username is None:
            username = email.split('@')[0]
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, username=None, password=None):
        if username is None:
            username = email.split('@')[0]
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
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
    first_name = models.CharField(
        verbose_name='first name',
        max_length=255,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
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
    bio = models.TextField(blank=True, null= True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
