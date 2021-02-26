from django.db import models
from django.template.defaultfilters import slugify


class Genres(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Genre name'
    )
    slug = models.SlugField(
        max_length=50,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Genre slug name'
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genres, self).save(*args, **kwargs)

    def __str__(self):
        return f'"{self.name}"'

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
