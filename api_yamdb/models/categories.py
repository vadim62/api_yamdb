from django.db import models


class Categories(models.Model):
    name = models.CharField(
        max_length=50,
    )
    slug = models.SlugField(
        max_length=50,
        null=False,
        unique=True,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['slug']
