from django.urls import path
from .views import chatbot_view, delete_chat

urlpatterns = [
    path("", chatbot_view, name="chatbot"),
    path("<int:chat_id>/", chatbot_view, name="chat_detail"),
    path("delete/<int:chat_id>/", delete_chat, name="delete_chat"),
]
