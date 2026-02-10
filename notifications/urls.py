from django.urls import path
from .views import notifications_list
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', notifications_list, name='list'),
    path('<int:pk>/mark-read/', views.mark_as_read, name='mark_read'),
    path('mark-all-read/', views.mark_all_as_read, name='mark_all_read'),
    path('<int:pk>/delete/', views.delete_notification, name='delete'),
]
