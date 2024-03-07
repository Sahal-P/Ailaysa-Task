from rest_framework import serializers
from .models import User

class UsersSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        contact_number (str): The contact number of the user.
        email (str): The email address of the user.
        profile_picture (str): The URL of the user's profile picture.
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'contact_number', 'email', 'profile_picture']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user