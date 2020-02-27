from django.contrib.auth import get_user_model
from rest_framework import serializers as sz


class BaseUserSerializer(sz.ModelSerializer):
    username = sz.CharField(max_length=20)
    password = sz.CharField(max_length=20,
                            style={'input_type': 'password'},
                            write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
