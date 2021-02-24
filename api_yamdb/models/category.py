from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
    )
    slug = models.SlugField(
        max_length=50,
        null=False,
        unique=True,
        primary_key=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['slug']