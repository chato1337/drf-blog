from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from faker import Faker
from rest_framework import status

faker = Faker()

class TestSetUp(APITestCase):
    def setUp(self):
        self.login_url = '/user/token/'
        self.my_password = 'park123'
        self.user = User.objects.create_superuser(
            first_name='test_name',
            last_name='testname',
            username='testname',
            password=self.my_password,
            email=faker.email()
        )

        # self.user.save()

        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'password': self.my_password
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()

        self.token = response.data['access']
        self.client.credentials(HTTP_AUTORIZATION='Bearer ' + self.token)
        return super().setUp()
