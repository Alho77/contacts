from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


User = get_user_model()


class UserModelTest(APITestCase):

    def test_create_user(self):
        """Test create user"""
        payload = {'username': 'test', 'password': '1234'}
        user = User.objects.create_user(**payload)

        self.assertEqual(user.username, payload['username'])
        self.assertEqual(len(User.objects.all()), 1)
        self.assertTrue(user.check_password(payload['password']))

    def test_create_superuser(self):
        """Test create user"""
        payload = {'username': 'test', 'password': '1234'}
        user = User.objects.create_superuser(**payload)

        self.assertEqual(user.username, payload['username'])
        self.assertEqual(len(User.objects.all()), 1)
        self.assertTrue(user.check_password(payload['password']))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_invalid(self):
        """Test create user with invalid inputs"""

        with self.assertRaises(ValueError):
            User.objects.create_user(None, None)
