# accounts/urls.py
from django.urls import path
from .views import RegisterUser, UserLoginView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),  # Add functionality to UserLoginView
]
