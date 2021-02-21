from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


from .title import Title
from .users import MyUser


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    text = models.TextField(
        max_length=300
    )
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        unique_together = ['author', 'title']

    def __str__(self):
        return f'"{self.text}"'
