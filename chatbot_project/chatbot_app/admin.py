from django.contrib import admin
from .models import ChatLog, ChatSession

# Register your models here.
admin.site.register(ChatLog)
admin.site.register(ChatSession)