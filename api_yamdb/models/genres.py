from django.db import models


class Genres(models.Model):
    name = models.CharField(
        max_length=50,
    )
    slug = models.SlugField(
        max_length=50,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return f'{self.slug}'

    class Meta:
        ordering = ['id']
