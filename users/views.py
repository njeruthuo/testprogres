from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.

from .serializers import UserModelSerializer
from .authentication import TokenAuthentication


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


user_create_view = UserCreateAPIView.as_view()


class UserLoginAPIView(APIView):
    serializer_class = UserModelSerializer
    # permission_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        # Get data from the request
        username_or_email = request.data.get('username')
        password = request.data.get('password')

        # Try to authenticate the user
        user = authenticate(
            request, username=username_or_email, password=password)

        if user is not None:
            # If authentication is successful, get or create a token for the user
            token, created = Token.objects.get_or_create(user=user)

            # Begin a session for the user
            login(request, user)

            # Respond with the user information and token
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)
        else:
            # If authentication fails, return an error
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


user_login_view = UserLoginAPIView.as_view()
