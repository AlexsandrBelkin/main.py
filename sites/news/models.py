from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    views = models.IntegerField()
    # image
    # comments
    # category

# todo Create new model for Commentary
#  create category model