from rest_framework import serializers
from .models import ChatSession, ChatLog

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = ['session_id']

class ChatLogSerializer(serializers.ModelSerializer):
    session = ChatSessionSerializer()

    class Meta:
        model = ChatLog
        fields = ['session', 'pdf_name', 'pdf_path', 'query_question', 'response_text']