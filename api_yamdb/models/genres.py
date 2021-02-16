from django.db import models
from django.template.defaultfilters import slugify


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

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Genres, self).save(*args, **kwargs)

    def __str__(self):
        return f'"{self.name}"'

    class Meta:
        ordering = ['id']