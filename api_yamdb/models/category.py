from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Category name'
    )
    slug = models.SlugField(
        max_length=50,
        null=False,
        unique=True,
        primary_key=True,
        verbose_name='slug name'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['slug', ]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
