from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    Title = models.CharField(max_length=200)
    Slug = models.SlugField(max_length=100, unique=True)
    Description = models.TextField()
    Thumbnail = models.ImageField(upload_to="blog/images")
    Publish = models.DateTimeField(default=timezone.now)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Status_choices = [
        {"Draft", "d"},
        {"Published", "p"}
    ]
    Status = models.CharField(max_length=10,
                              choices=Status_choices,
                              default="d")
