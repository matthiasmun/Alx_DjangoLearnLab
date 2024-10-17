from rest_framework import serializers
from .models import User  # Adjust this import according to your user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Or specify the fields you want to include
