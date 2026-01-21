from django.shortcuts import render

def diseases(request):
    return render(request, 'diseases/diseases.html')
