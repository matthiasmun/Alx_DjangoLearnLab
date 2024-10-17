from django.urls import path
from .views import RegisterUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
]

from django.urls import path
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    # Add more URLs for profile management as needed
]
