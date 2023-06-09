from rest_framework import serializers
from auth_user.models import Profile, Role
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = []