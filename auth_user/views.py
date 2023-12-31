from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from auth_user.serializers import ProfileSerializer, RoleSerializer, UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()


class ProfielViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = RoleSerializer.Meta.model.objects.all()

