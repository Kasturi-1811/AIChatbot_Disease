from django.urls import path
from . import views
from .views import save_quiz_result

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('save-result/', save_quiz_result, name='save_quiz_result'),
]
