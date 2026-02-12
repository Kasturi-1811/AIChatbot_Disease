from django.db import models
from apps.accounts.models import CustomUser

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    added_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="quizzes_added"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
