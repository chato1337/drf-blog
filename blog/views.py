from django.shortcuts import render
from rest_framework import viewsets

from blog.serializers import CommentSerialzer, PostSerializer, TagSerializer
from django_filters import rest_framework as filters

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = PostSerializer
    filterset_fields = ('subject', 'author')
    queryset = PostSerializer.Meta.model.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerialzer
    queryset = CommentSerialzer.Meta.model.objects.all()

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = TagSerializer.Meta.model.objects.all()