from django.db import models


class ChatSession(models.Model):
    session_id = models.CharField(max_length=255)


class ChatLog(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    pdf_name = models.CharField(max_length=255, blank=True, null=True)
    query_question = models.TextField()
    response_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"ChatLog - {self.session.session_id} - {self.pdf_name}"