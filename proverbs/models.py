from django.db import models


class Proverb(models.Model):
    content = models.TextField()
    slug = models.SlugField()
    order = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.order}: {self.slug}"
