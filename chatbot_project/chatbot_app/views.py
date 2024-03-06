# views.py
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import ChatSession, ChatLog
from .serializers import ChatSessionSerializer, ChatLogSerializer
from .chatbot_utils import process_question

@api_view(['GET'])
def check_session_exists(request, session_id):
    try:
        session = ChatSession.objects.get(session_id=session_id)
        serializer = ChatSessionSerializer(session)
        return Response(serializer.data)
    except ChatSession.DoesNotExist:
        return Response({"session_exists": False})

@api_view(['POST'])
def chatlog_list_create_view(request, session_id, pdf_name=None, query_question=None):
    if pdf_name:
        # New session with PDF, process the question and update/create the ChatLog
        pdf_path = os.path.abspath(os.path.join(BASE_DIR, "uploads", pdf_name))
        pdf_text = extract_text_from_pdf(pdf_path)
        response_text = process_question(session_id, pdf_text, query_question)
        chatlog, created = ChatLog.objects.get_or_create(
            session_id=session_id,
            pdf_name=pdf_name,
            query_question=query_question,
            defaults={'response_text': response_text}
        )
    else:
        # Existing session without PDF, retrieve old chats and process the question
        old_chats = ChatLog.objects.filter(session_id=session_id).values_list('response_text', flat=True)
        response_text = process_question(session_id, old_chats[-1] if old_chats else None, query_question)
        chatlog = ChatLog.objects.create(
            session_id=session_id,
            pdf_name=None,
            query_question=query_question,
            response_text=response_text
        )

    serializer = ChatLogSerializer(chatlog)

    return JsonResponse({
        'old_chats': list(old_chats),
        'new_chat': serializer.data['response_text'],

    })
