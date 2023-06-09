from rest_framework import serializers
from blog.models import Post, Comment, Tag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []

class CommentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = []

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = []
