from django.urls import path
from .views import symptom_checker_view

app_name = "symptom_checker"

urlpatterns = [
    path("", symptom_checker_view, name="symptom_checker"),
]
