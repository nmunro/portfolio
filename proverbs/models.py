from django.db import models


class Proverb(models.Model):
    content = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.slug
