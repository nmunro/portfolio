from django.db import models


class Employer(models.Model):
    class Meta:
        verbose_name_plural = "Employer"

    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    started = models.DateField()
    ended = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.company
