from django.utils import translation
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.conf import settings

class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_lang = None
        if request.user.is_authenticated and hasattr(request.user, 'language'):
            user_lang = request.user.language

        if not user_lang:
            # Use browser language or default
            user_lang = request.COOKIES.get('django_language', settings.LANGUAGE_CODE)

        translation.activate(user_lang)
        request.LANGUAGE_CODE = user_lang

        response = self.get_response(request)

        # Set language cookie
        response.set_cookie('django_language', user_lang)

        return response