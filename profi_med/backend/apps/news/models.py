from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField("слаг", max_length=60, unique=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Специалисты"
        ordering = ['name']
    def __str__(self):
        return self.name