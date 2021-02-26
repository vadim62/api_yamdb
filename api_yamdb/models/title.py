import datetime as dt

from django.core.validators import MaxValueValidator
from django.db import models

from .category import Category
from .genre import Genre


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
