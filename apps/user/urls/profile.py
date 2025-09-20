from django.urls import path

from apps.user.views.profile import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    ]