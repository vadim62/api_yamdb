from django.core.validators import MaxValueValidator
from django.db import models

from .titles import Titles
from .users import MyUser


class Review(models.Model):
    score = models.PositiveIntegerField(
        validators=[MaxValueValidator(10)]
    )
    title_id = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField(
        max_length=300
    )
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='reviews')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    def __str__(self):
        return f'"{self.text}"'

    class Meta:
        ordering = ['id']
