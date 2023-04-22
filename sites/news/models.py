from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)


class News(models.Model):
    title = models.CharField(max_length=50)
    picture = models.FileField(upload_to="news/static/news/img/")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
# todo create category model


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()