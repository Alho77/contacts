from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class EmailActivationToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return super()._make_hash_value(user, timestamp)
