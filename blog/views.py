from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from auth_user.models import Profile
from blog.models import Comment
from blog.serializers import CommentSerialzer, PostSerializer, TagSerializer
from django_filters import rest_framework as filters
from django.core.exceptions import ObjectDoesNotExist

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

class LikeViewSet(viewsets.GenericViewSet):
    serializer_class = CommentSerialzer
    queryset = CommentSerialzer.Meta.model.objects.all()

    def update(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
            profile = Profile.objects.get(pk=request.data['profile'])
            comment.likes.add(profile)
        except ObjectDoesNotExist:
            return Response({'success': 'failed liked comment'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'liked comment!'}, status=status.HTTP_200_OK)