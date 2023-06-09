from rest_framework import serializers
from auth_user.models import Profile, Role

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = []