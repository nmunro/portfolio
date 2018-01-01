from django.db import models


class Qualification(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Education(models.Model):
    class Meta:
        verbose_name_plural = "Education"

    institution = models.CharField(max_length=255)
    qualification = models.ForeignKey(to='education.Qualification', on_delete=models.CASCADE)
    course = models.CharField(max_length=255)
    enrolled = models.DateField()
    completed = models.DateField()    
    description = models.TextField()

    def __str__(self):
        return self.institution
