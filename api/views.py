from django.shortcuts import render
from rest_framework import views, response, exceptions, permissions, generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, ChatBotSerializer, LoginSerializer
from . import models
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegisterView(views.APIView):
    
    def post (self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        token = RefreshToken.for_user(user=user)
        data = serializer.data
        data['token'] = {"access": str(token.access_token), "refresh": str(token)}
        return Response(data, status=status.HTTP_200_OK)

class Login(views.APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['token'] = {"access": str(token.access_token), "refresh": str(token)}
        return Response(data, status=status.HTTP_200_OK)

class GetUser(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
    
class ChatBotAllocated(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = models.Chatbot
    serializer_class = ChatBotSerializer
    
    def get_queryset(self):
        queryset = models.Chatbot.objects.filter(owner_id = self.request.user.id)
        return queryset
    
class UpdateAndRetrive(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChatBotSerializer
    
    def get_queryset(self):
        queryset = models.Chatbot.objects.filter(owner_id = self.request.user.id)
        return queryset