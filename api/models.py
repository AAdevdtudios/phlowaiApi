from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField
from .manager import CustomUserManager

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Chatbot(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    json_obj = models.TextField(null=True)
    
    def __str__(self):
        return self.name

class Website(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chatbot_id = models.ForeignKey(Chatbot, on_delete=models.CASCADE)
    json_obj = models.TextField(null=True)
    
    def __str__(self):
        return self.name