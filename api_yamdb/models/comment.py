from django.contrib.auth import get_user_model
from django.db import models

from .review import Review

User = get_user_model()


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
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
