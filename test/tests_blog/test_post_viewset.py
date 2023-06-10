from test.factories.post_factories import PostFactory
from test.test_setup import TestSetUp
from rest_framework import status

class PostTestCase(TestSetUp):
    url = '/blog/post/'

    def test_get_posts(self):
        response = self.client.get(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        response = self.client.post(
            self.url,
            PostFactory().build_post_JSON(),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_bad(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CommetTestCase(TestSetUp):
    url = '/blog/comment/'
    def test_get_comment(self):
        response = self.client.get(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_comment(self):
        response = self.client.post(
            self.url,
            PostFactory().build_comment_JSON(),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TagTestCase(TestSetUp):
    url = '/blog/tag/'
    def test_get_tags(self):
        response = self.client.get(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tag(self):
        response = self.client.post(
            self.url,
            PostFactory().build_tag_JSON(),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_tag_bad(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LikeTestCase(TestSetUp):
    url = '/blog/like/1/'
    def test_like_comment(self):
        # import pdb; pdb.set_trace()
        comment = PostFactory().create_comment()
        response = self.client.put(self.url, {"profile": 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
