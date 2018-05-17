from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Article(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Mete:
        ordering = ("-publish", )

    def __str__(self):
        return self.title