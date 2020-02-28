from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# class ContactManager(models.Manager):

#     def create(self, name, user, **extra_fields):
#         """Create contact object and add current authenticated user for user field"""
#         contact = self.model(name=name, user=user)


class Contact(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    birth_date = models.DateField(auto_now=True, blank=True)
    description = models.TextField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    contact = models.ForeignKey(to=Contact, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
