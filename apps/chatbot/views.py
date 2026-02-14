# chatbot/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat, Message
from .gemini_client import generate_reply

import markdown
from django.utils.safestring import mark_safe
from django.utils import translation


def chatbot_view(request, chat_id=None):
    chats = Chat.objects.all().order_by("-created_at")

    if chat_id:
        chat = get_object_or_404(Chat, id=chat_id)
    else:
        chat = Chat.objects.create(title="New Chat")
        return redirect("chatbot:chat_detail", chat_id=chat.id)

    if request.method == "POST":
        user_msg = request.POST.get("message")

        # Save user message
        Message.objects.create(
            chat=chat,
            role="user",
            text=user_msg
        )

        # Build conversation for Gemini
        conversation = ""
        for msg in chat.messages.all():
            role = "User" if msg.role == "user" else "AI"
            conversation += f"{role}: {msg.text}\n"
        
        current_language = translation.get_language()

        # Get AI reply
        ai_reply = generate_reply(conversation,current_language)

        # Convert Markdown → HTML
        html_reply = mark_safe(markdown.markdown(ai_reply))

        # Save AI message
        Message.objects.create(
            chat=chat,
            role="ai",
            text=html_reply
        )

        # Set chat title from first message
        if chat.title == "New Chat":
            chat.title = user_msg[:30]
            chat.save()

    return render(request, "chatbot/chatbot.html", {
        "chat": chat,
        "chats": chats,
    })


def delete_chat(request, chat_id):
    chat_to_delete = get_object_or_404(Chat, id=chat_id)

    # get remaining chats BEFORE delete
    remaining_chats = Chat.objects.exclude(id=chat_id).order_by("-created_at")

    chat_to_delete.delete()

    # If user deleted the currently open chat
    if str(chat_id) == request.GET.get("current"):
        if remaining_chats.exists():
            return redirect("chatbot:chat_detail", chat_id=remaining_chats.first().id)
        else:
            return redirect("chatbot:chatbot")  # will create ONE new chat
    
    # If deleted some other chat, stay on same page
    return redirect(request.META.get("HTTP_REFERER", "chatbot:chatbot"))
