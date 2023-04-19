from django.contrib import admin
from .models import Chatbot, Website, User
# Register your models here.

admin.site.register(Chatbot)
admin.site.register(User)
admin.site.register(Website)