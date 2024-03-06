from rest_framework import serializers
from .models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'contact_number', 'email', 'profile_picture']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user