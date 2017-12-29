from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    published_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name="blogs")

    def __str__(self):
        return self.title
