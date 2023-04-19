from django.urls import path
from .views import RegisterView, GetUser, ChatBotAllocated, Login, UpdateAndRetrive
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', Login.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
    path('', GetUser.as_view()),
    path('chatbot', ChatBotAllocated.as_view()),
    path('chatbot/<int:pk>', UpdateAndRetrive.as_view()),
]
