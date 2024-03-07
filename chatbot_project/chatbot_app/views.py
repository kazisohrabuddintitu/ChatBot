from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import ChatSession, ChatLog
from .serializers import ChatSessionSerializer, ChatLogSerializer
from .chatbot_utils import process_question
import os
from django.conf import settings

BASE_DIR = settings.BASE_DIR


# function for existing pdf, session id with new question
class ChatLogCreateView(APIView):
    def post(self, request, session_id, query_question, format=None):
        query_question = request.data.get('query_question', query_question)

        # Check if a ChatLog with the given session ID exists
        chat_logs = ChatLog.objects.filter(session_id=session_id)

        if chat_logs.exists():
            pdf_name = chat_logs.first().pdf_name
        else:
            pdf_name = None

        # Get old chats before saving the new entry
        old_chats = chat_logs.values_list('response_text', flat=True)
       
        print("query question: ", query_question)
        response_text = process_question(session_id, pdf_name, query_question)
       
        # Save to the database with the nested serializer data
        serializer = ChatLogSerializer(data={'session': {'session_id': session_id}, 'pdf_name': pdf_name, 'query_question': query_question, 'response_text': response_text})
        if serializer.is_valid():
            serializer.save()

            # Return information about old chats along with the new chat
            serializer_data = serializer.data
            serializer_data['old_chats'] = list(old_chats)
            return Response(serializer_data)
        else:
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=400)


# view for new pdf with new session id and question 
class NewChatLogCreateView(APIView):
    def post(self, request, session_id, pdf_name, query_question, format=None):
        print("calling new chat")
        # Calling chatbot utility function
        response_text = process_question(session_id, pdf_name, query_question)
        
        # Save to database
        serializer = ChatLogSerializer(data={'session': {'session_id': session_id}, 'pdf_name': pdf_name, 'query_question': query_question, 'response_text': response_text})
        if serializer.is_valid():
            serializer.save()
            return Response({"response_text": response_text})
        else:
            return Response(serializer.errors, status=400)
