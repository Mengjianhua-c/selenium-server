from django.shortcuts import render
from taskApi.models.task import TaskSerializers, Task
from rest_framework import viewsets


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
