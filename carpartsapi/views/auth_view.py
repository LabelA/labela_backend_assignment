import logging

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterApiView(APIView):
    logger = logging.getLogger(__name__)

    def post(self, request):
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        email = request.data.get('email')
        if password1 != password2:
            return Response("password mismatch", status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response("user already exist please login", status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        return Response("user registration success", status=status.HTTP_201_CREATED)
