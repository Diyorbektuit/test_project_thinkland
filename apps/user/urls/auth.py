from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from apps.user.views.auth import RegisterView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view()),
    ]