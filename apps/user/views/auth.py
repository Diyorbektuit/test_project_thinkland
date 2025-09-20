from rest_framework import generics

from apps.user.serializer.auth import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

