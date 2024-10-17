# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser  # Ensure CustomUser is correctly imported

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # Use CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
