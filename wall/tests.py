from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status, test, exceptions

from .models import Message


class WallTests(test.APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'test1', 'test@email.com', 'test@123')

        self.user2 = User.objects.create_user(
            'test2', 'test2@email.com', 'test@123')

        self.message = Message.objects.create(
            author_id=1, title="test 1", body="lalalalala123123")

        self.message = Message.objects.create(
            author_id=2, title="test 2", body="mimimimimi123123")

        self.wall_list_url = reverse('wall_list')
        self.wall_details_url = reverse('wall_details', kwargs={'pk': 1})

    def test_can_get_posts_on_wall(self):
        """
        Ensure we can get posts on the wall, even if we are not logged in.
        """
        response = self.client.get(self.wall_list_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'test 2')
        self.assertEqual(response.data[0]['body'], 'mimimimimi123123')
        self.assertEqual(response.data[1]['title'], 'test 1')
        self.assertEqual(response.data[1]['body'], 'lalalalala123123')

    def test_cannot_create_new_post_on_wall(self):
        """
        Ensure we cannot create a new post on the wall if we are not logged in
        """
        request_data = {
            'title': 'lalalalalalalalala',
            'body': 'mimimimimimimimimimi',
        }

        response = self.client.post(
            self.wall_list_url, request_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'detail': exceptions.ErrorDetail(
            string='Authentication credentials were not provided.', code='not_authenticated')})

    def test_can_create_new_post_on_wall(self):
        """
        Ensure we can create a new post on the wall, only if we are logged in
        """
        request_data = {
            'title': 'lalalalalalalalala',
            'body': 'mimimimimimimimimimi',
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            self.wall_list_url, request_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author'], 'test1')
        self.assertEqual(response.data['title'], 'lalalalalalalalala')
        self.assertEqual(response.data['body'], 'mimimimimimimimimimi')

    def test_cannot_delete_post_on_wall(self):
        """
        Ensure we cannot delete a post if we are not logged in or we are not the post's owner
        """

        response = self.client.delete(self.wall_details_url, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)

        response = self.client.delete(self.wall_details_url, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_can_delete_post_on_wall(self):
        """
        Ensure we can delete a post only if we are the post's owner and we are logged in
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(self.wall_details_url, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)

    def test_cannot_edit_post_on_wall(self):
        """
        Ensure we cannot edit a post if we are not logged in or we are not the post's owner
        """

        response = self.client.put(self.wall_details_url, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)

        response = self.client.put(self.wall_details_url, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_can_edit_post_on_wall(self):
        """
        Ensure we can edit a post only if we are the post's owner and we are logged in
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.put(self.wall_details_url, {
                                   'title': 'test 3'}, format='json')

        self.assertEqual(response.data['title'], 'test 3')
        self.assertEqual(response.data['body'], 'lalalalala123123')
