# chatbot/models.py
from django.db import models

class Chat(models.Model):
    title = models.CharField(max_length=100, default="New Chat")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=10)  # user / ai
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
