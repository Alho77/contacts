from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework import status
from rest_framework.views import APIView, Response

from user.api.serializers import BaseUserSerializer

User = get_user_model()


class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = BaseUserSerializer(instance=users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SignUpView(APIView):

    def post(self, request):
        serializer = BaseUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Invalid credentials', status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        serializer = BaseUserSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('Invalid credentials', status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
