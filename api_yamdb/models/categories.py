from django.db import models
from django.template.defaultfilters import slugify


class Categories(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        blank=True,
        null=False,
        unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)

    def __str__(self):
        return f'"{self.name}"'
