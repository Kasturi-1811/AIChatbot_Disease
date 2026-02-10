from django.urls import path
from .views import vaccination, add_vaccination

urlpatterns = [
    path('', vaccination, name='vaccination'),
    path('add/', add_vaccination, name='add_vaccination'),
]
