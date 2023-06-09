from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    bio = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    user = models.ForeignKey(User, related_name="profile", blank=True, on_delete=models.CASCADE)

class Role(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.ManyToManyField(User, related_name="role", blank=True)
