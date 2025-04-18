from django.db import models


class Priority(models.IntegerChoices):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    priority = models.IntegerField(choices=Priority.choices, db_index=True)
    due_date = models.DateField(null=True, db_index=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
