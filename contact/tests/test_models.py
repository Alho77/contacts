from django.contrib.auth import get_user_model
from django.test import TestCase

from contact.models import Contact, Email, Phone

User = get_user_model()


class ContactModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('test', '1234')

    def test_create_contact(self):
        """Test creating contact"""
        payload = {
            'name': 'con',
            'phone': ['12345678', '12345679'],
            'email': ['cont@test.com', ],
            'user': self.user
        }
        cont = Contact.objects.create(**payload)

        self.assertEqual(cont.name, payload['name'])
        self.assertEqual(cont.user, payload['user'])
        self.assertEqual(len(Contact.objects.all()), 1)
        self.assertEqual(len(Phone.objects.filter(contact=cont)), 2)
        self.assertEqual(len(Email.objects.filter(contact=cont)), 1)
