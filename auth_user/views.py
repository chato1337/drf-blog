from django.shortcuts import render
from rest_framework import viewsets

from auth_user.serializers import ProfileSerializer, RoleSerializer

# Create your views here.
class ProfielViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = RoleSerializer.Meta.model.objects.all()

