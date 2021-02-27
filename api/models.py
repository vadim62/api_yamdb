import datetime as dt

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
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
        if self.role == self.PermissionChoice.USER:
            return True
        return False

    @property
    def is_moderator(self):
        'Returns True if user has role moderator.'
        if self.role == self.PermissionChoice.MODERATOR:
            return True
        return False

    @property
    def is_admin(self):
        'Returns True if user has role admin.'
        if self.role == self.PermissionChoice.ADMIN or self.is_staff is True:
            return True
        return False


User = get_user_model()


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Genre name'
    )
    slug = models.SlugField(
        max_length=50,
        blank=False,
        null=False,
        unique=True,
        db_index=True,
        primary_key=True,
        verbose_name='Genre slug name'
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['slug', ]


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Category name'
    )
    slug = models.SlugField(
        max_length=50,
        null=False,
        unique=True,
        primary_key=True,
        verbose_name='slug name'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['slug', ]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Title(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Title name'
    )
    year = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(dt.datetime.now().year + 1)],
        verbose_name='Year of production'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True,
        verbose_name='Title category'
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Title description'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Title genres'
    )

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Review title'
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Rating'
    )
    text = models.TextField(
        max_length=300,
        verbose_name='Review text'
    )
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Review author'
    )
    pub_date = models.DateTimeField(
        verbose_name='Date published',
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique author_title')
        ]
        ordering = ['id', ]
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'"{self.text}"'


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Review'
    )
    text = models.TextField(
        max_length=300,
        verbose_name='Review text'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Review author'
    )
    pub_date = models.DateTimeField(
        verbose_name='Date published',
        auto_now_add=True
    )

    def __str__(self):
        return f'"{self.text}"'

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
