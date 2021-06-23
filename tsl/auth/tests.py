from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail

from rest_framework import status, test

from jwt import decode


class AuthTests(test.APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'test1', 'test@email.com', 'test@123')

        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_get_token_with_user_details(self):
        response = self.client.post(
            self.login_url, {'username': 'test1', 'password': 'test@123'}, format='json')

        decoded_token = decode(
            response.data['access'], key='django-insecure-$dld*x3rd)bfyt*wutxj_qg(q+^^(r2_nt1*gyjjjivem82^yz', algorithms=['HS256'])
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(decoded_token['username'], 'test1')

    def test_can_send_email_when_new_user_register(self):
        """
        Ensure we can send an email to the user when it's registered
        """
        with self.settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'):
            request_data = {
                'username': 'test2',
                'password': 'test@123',
                'password2': 'test@123',
                'email': 'test2@email.com',
                'first_name': 'Test',
                'last_name': 'Mock',
            }
            response = self.client.post(
                self.register_url, request_data, format='json')

            self.assertEquals(response.status_code, status.HTTP_201_CREATED)
            self.assertEquals(len(mail.outbox), 1)
            self.assertEquals(
                mail.outbox[0].subject, 'Congratulations! Your user - test2 - was created at Wall App')
            self.assertEquals(
                mail.outbox[0].body, 'Hello Test Mock, now you can login at Wall App using username and password that you created.')
