
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    empId = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    subjects = models.ManyToManyField(Subject, related_name="trainers")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - ({self.empId})"