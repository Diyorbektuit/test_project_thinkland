from rest_framework import generics

from apps.user.serializer.profile import ProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    http_method_names = ('get', 'patch', )

    def get_object(self):
        return self.request.user
