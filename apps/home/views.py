from django.shortcuts import render

def home(request):
    context = {
        'user': request.user  # Pass user to template
    }
    return render(request, 'home/home.html', context)