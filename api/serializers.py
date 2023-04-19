from rest_framework import serializers
from .models import User, Chatbot
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserSerializer():
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only = True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if not email or not password:
            raise serializers.ValidationError("Please provide email and password")
        
        if User.objects.filter(email= email).exists():
            raise serializers.ValidationError("Email already exist")
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only = True)
    name = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credential")
    
class ChatBotSerializer(serializers.ModelSerializer):
    #owner_id = User.objects.get(email = request)
    class Meta:
        model = Chatbot
        fields = '__all__'