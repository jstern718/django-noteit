import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True, default="")
    content = models.TextField(max_length=10000, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL,
                               blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}: {self.content[0:50]}"

    def was_published_recently(self):
        return self.updated_at >= timezone.now() - datetime.timedelta(days=1)





