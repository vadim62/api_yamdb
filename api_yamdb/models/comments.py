from django.db import models

from .review import Review
from .users import MyUser
from .titles import Titles


class Comments(models.Model):
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        max_length=300
    )
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='comments')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    def __str__(self):
        return f'"{self.text}"'

    class Meta:
        ordering = ['id']
