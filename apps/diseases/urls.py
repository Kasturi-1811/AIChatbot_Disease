from django.urls import path
from . import views
from .views import diseases, add_disease

urlpatterns = [
    path('', views.diseases, name='diseases'),
    path('add/', add_disease, name='add_disease'),
]
