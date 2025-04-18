from rest_framework import viewsets

from task_manager.tasks.models import Task


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = AccountSerializer
    