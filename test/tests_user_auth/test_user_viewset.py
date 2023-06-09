from test.test_setup import TestSetUp
from rest_framework import status
from test.factories.user_factories import UserFactory

class UserTestCase(TestSetUp):
    url = '/user/user/'
    def test_get_users(self):
        response = self.client.get(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        response = self.client.post(
            self.url,
            UserFactory().build_user_JSON(),
            format='json'
        )
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(len(response.data), 1)

    def test_create_user_bad(self):
        response = self.client.post(
            self.url,
            {},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ProfileTestCase(TestSetUp):
    url = '/user/profile/'
    def test_get_users(self):
        response = self.client.get(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):

        response = self.client.post(
            self.url,
            UserFactory().build_profile_JSON(),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_user_bad(self):
        response = self.client.post(
            self.url,
            {},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class RoleTestCase(TestSetUp):
    url = '/user/role/'
    def test_get_roles(self):
        response = self.client.get(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_role(self):
        response = self.client.post(self.url, UserFactory().build_role_JSON(), format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_role_bad(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
