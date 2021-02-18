from django.db import models
from django.template.defaultfilters import slugify


class Categories(models.Model):
    name = models.CharField(
        max_length=50,
        # unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        # blank=True,
        null=False,
        unique=True
    )

    def __str__(self):
        return f'"{self.name}"'

    class Meta:
        ordering = ['id']
