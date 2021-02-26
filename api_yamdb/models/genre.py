from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
    )
    slug = models.SlugField(
        max_length=50,
        blank=False,
        null=False,
        unique=True,
        db_index=True,
        primary_key=True
    )

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['slug', ]
