from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db.utils import IntegrityError

from user.models import Email, Phone

User = get_user_model()


class UserModelTest(TestCase):

    def test_create_user(self):
        """Test create user"""
        payload = {
            'username': 'test',
            'password': '1234',
            'phone': ['12345678', '12345679'],
            'email': ['test@test.com', ]
        }
        user = User.objects.create_user(**payload)

        self.assertEqual(user.username, payload['username'])
        self.assertEqual(len(User.objects.all()), 1)
        self.assertEqual(len(Phone.objects.filter(user=user)), 2)
        self.assertEqual(len(Email.objects.filter(user=user)), 1)
        self.assertTrue(user.check_password(payload['password']))

    def test_create_user_duplicate(self):
        """Test create user with duplicate entries for phone and email"""
        payload = {
            'username': 'test',
            'password': '1234',
            'phone': ['12345678', '12345678'],
            'email': ['test@test.com', 'test@test.com']
        }

        with self.assertRaises(IntegrityError):
            User.objects.create_user(**payload)

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
