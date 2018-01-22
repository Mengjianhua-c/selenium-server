from django.shortcuts import render
from taskApi.models.task import TaskSerializers, Task

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class TaskList(APIView):

    def post(self, request):
        page = request.data
        print(page)
        tasks = Task.objects.all()
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)


class CreateTask(APIView):
    def post(self, request, format=None):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors)
