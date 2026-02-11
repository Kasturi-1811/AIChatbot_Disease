from django.urls import path
from . import views
from .views import diseases, add_disease

urlpatterns = [
    path('', views.diseases, name='diseases'),
    path('add/', add_disease, name='add_disease'),
    path('library/', views.disease_library, name='disease_library'),
    path('library/<int:pk>/', views.disease_detail, name='disease_detail'),
    path('library/add/', views.add_library_disease, name='add_library_disease'),
    


]
