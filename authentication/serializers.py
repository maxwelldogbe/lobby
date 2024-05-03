from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['__all__']
        
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=User.CATEGORY_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'category']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        category = validated_data['category']
        User.objects.create(user=user, category=category)
        return user