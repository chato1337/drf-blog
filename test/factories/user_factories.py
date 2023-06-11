from django.contrib.auth.models import User
from auth_user.models import Profile
from faker import Faker

class UserFactory:
    def build_user_JSON(self):
        faker = Faker()
        name = faker.profile()['username']
        return {
            'username': name,
            'email': 'me@me.com',
            'password': 'asd123.'
        }

    def build_profile_JSON(self):
        user = self.create_user()
        return {
            "bio": "string",
            "image": "string",
            "user": user.pk
        }

    def build_role_JSON(self):
        user = self.create_user()
        return {
            'name': 'role test',
            'user': [user.pk]
        }

    def create_user(self):
        return User.objects.create(**self.build_user_JSON())

    def create_profile(self):
        profile_dict = self.build_profile_JSON()
        user = User.objects.get(pk=profile_dict['user'])
        return Profile.objects.create(**{**profile_dict, 'user': user})