from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title import Title
from .users import MyUser


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
        unique_together = ['author', 'title', ]
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'"{self.text}"'
