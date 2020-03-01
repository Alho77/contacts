from datetime import data, timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

from user import tokens


class TokenGeneratorTest(TestCase):

    def test_create_token(self):
        """
        Test that created token is valid
        """
