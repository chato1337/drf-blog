from django.contrib.auth.models import User
from auth_user.models import Profile

class UserFactory:
    def build_user_JSON(self):
        return {
            'username': 'test_user',
            'email': 'me@me.com',
            'password': 'asd123.'
        }

    def build_profile_JSON(self):
        user = self.create_user()
        return {
            "bio": "string",
            "image": "string",
            "user": 1
        }

    def build_role_JSON(self):
        user = self.create_user()
        return {
            'name': 'role test',
            'user': [1]
        }

    def create_user(self):
        return User.objects.create(**self.build_user_JSON())

    def create_profile(self):
        profile_dict = self.build_profile_JSON()
        user = User.objects.get(pk=profile_dict['user'])
        return Profile.objects.create(**{**profile_dict, 'user': user})