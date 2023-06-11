from auth_user.models import Profile
from blog.models import Comment, Post
from test.factories.user_factories import UserFactory


class PostFactory:
    def build_post_JSON(self):
        # user = UserFactory().create_user()
        profile = UserFactory().create_profile()
        return {
            'content': 'post test',
            'subject': 'subject test',
            'author': profile.pk
        }
    def build_comment_JSON(self):
        post = self.create_post()
        profile = UserFactory().create_profile()
        return {
            "content": "string",
            "author": profile.pk,
            "post": post.pk,
            "likes": []
        }

    def build_tag_JSON(self):
        post = self.create_post()
        return {
            "name": "my_tag",
            "posts": [post.pk]
        }

    def create_post(self):
        post_dict = self.build_post_JSON()
        author = Profile.objects.get(pk=post_dict['author'])
        return Post.objects.create(**{**post_dict, 'author': author})

    def create_comment(self):
        comment_dict = self.build_comment_JSON()
        del comment_dict['likes']
        author = Profile.objects.get(pk=comment_dict['author'])
        post = Post.objects.get(pk=comment_dict['post'])
        return Comment.objects.create(**{**comment_dict, 'author': author, 'post': post})