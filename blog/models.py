from django.db import models

from auth_user.models import Profile

# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=64, unique=True)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=60)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Profile, related_name="liked", blank=True)
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=64)
    posts = models.ManyToManyField(Post, related_name="tags", blank=True)