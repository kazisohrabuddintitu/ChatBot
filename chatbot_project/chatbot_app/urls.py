from django.urls import path
from .views import ChatLogCreateView, NewChatLogCreateView

urlpatterns = [
    path('chatlog/<str:session_id>/<str:query_question>/', ChatLogCreateView.as_view(), name='chatlog-create'),
    path('new_chatlog/<str:session_id>/<str:pdf_name>/<str:query_question>/', NewChatLogCreateView.as_view(), name='new-chatlog-create'),
]
