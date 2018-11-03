from django.contrib.auth.models import User
from django.db import models


class Thread(models.Model):
    title = models.CharField(max_length=255)
    restricted = models.BooleanField(default=False)


class Post(models.Model):
    class Meta:
        ordering = ['created_at']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
