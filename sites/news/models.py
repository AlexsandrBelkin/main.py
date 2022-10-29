from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    views = models.IntegerField()
    # image
# todo create category model


class Commentary(models.Model):
    ip = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

