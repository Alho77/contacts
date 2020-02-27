from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from user.api import views

User = get_user_model()

RETRIVE_URL = reverse('user:list')
SIGNUP_URL = reverse('user:register')
LOGIN_URL = reverse('user:login')


class PublicUserTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('test', '1234')
        self.client = APIClient()

    def test_user_retrive(self):
        """Test retrive all users"""
        res = self.client.get(RETRIVE_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(User.objects.all()), 1)

    def test_user_register(self):
        """Test register user"""
        payload = {'username': 'test1', 'password': '1234'}
        res = self.client.post(SIGNUP_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['username'], payload['username'])
        self.assertEqual(len(User.objects.all()), 2)
        self.assertNotIn('password', res.data)

    def test_user_login(self):
        """Test login user"""
        payload = {'username': 'test', 'password': '1234'}
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['username'], payload['username'])
        self.assertNotIn('password', res.data)


class PrivateUserTest(APITestCase):
    """Test private methodes for user"""

    def setUp(self):
        self.user = User.objects.create_user('test', '1234')
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.client.force_authenticate(self.user)

    def test_user_logout(self):
        """Test logout user"""
        logout_view = views.LogoutView.as_view()
        logout_path = reverse('user:logout')
        # FIXME: session error for request, doesn't have session authentication
        request = self.factory.post(logout_path)
        request.user = self.user
        res = logout_view(request)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user.is_authenticated)
        self.assertFalse(self.user.is_active)
