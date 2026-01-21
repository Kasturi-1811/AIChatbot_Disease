from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def quiz(request):
    return render(request, 'quiz/quiz.html')
