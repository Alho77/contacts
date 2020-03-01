from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):

        if username is None or password is None:
            raise ValueError('Invalid inputs')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if extra_fields.__contains__('phone'):
            phone = extra_fields['phone']
            for entry in phone:
                Phone.objects.create(user=user, phone=entry)

        if extra_fields.__contains__('email'):
            email = extra_fields['email']
            for entry in email:
                Email.objects.create(user=user, email=entry)

        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    birth_data = models.DateField(blank=True, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.username


class Phone(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    phone = models.IntegerField(unique=True)
    confirmed = models.BooleanField(default=False, verbose_name='confirmed')


class Email(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="Emails")
    email = models.EmailField(unique=True, max_length=30)
    confirmed = models.BooleanField(default=False, verbose_name='confirmed')
