from django.urls import path
from .views import chatlog_list_create_view, check_session_exists


urlpatterns = [
    path('chatlog/<str:session_id>/', chatlog_list_create_view, name='chatlog-list-create'),
    path('check_session_exists/<str:session_id>/', check_session_exists, name='session id check')
]