import datetime as dt

from django.core.validators import MaxValueValidator
from django.db import models

from .categories import Categories


class Titles(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(dt.datetime.now().year+1)]
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )
