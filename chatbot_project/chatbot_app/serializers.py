from rest_framework import serializers
from .models import ChatSession, ChatLog

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = ['session_id']


class ChatLogSerializer(serializers.ModelSerializer):
    session = ChatSessionSerializer()
    old_chats = serializers.ListField(child=serializers.CharField(), read_only=True)

    class Meta:
        model = ChatLog
        fields = ['session', 'pdf_name', 'query_question', 'response_text', 'old_chats']

    def create(self, validated_data):
        session_data = validated_data.pop('session', None)

        # Creating or retrieving the ChatSession instance
        if session_data:
            session_instance, _ = ChatSession.objects.get_or_create(**session_data)
        else:
            session_instance = None

        # Creating the ChatLog instance with the retrieved or created session
        chat_log_instance = ChatLog.objects.create(session=session_instance, **validated_data)

        return chat_log_instance
