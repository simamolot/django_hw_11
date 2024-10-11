from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.task import SubTask
from .serializers.task import SubTaskDetailSerializer
from django.http import Http404

class SubTaskListCreateView(APIView):
    def get(self, request):
        sub_tasks = SubTask.objects.all()
        serializer = SubTaskDetailSerializer(sub_tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubTaskDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SubTaskDetailUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sub_task = self.get_object(pk)
        serializer = SubTaskDetailSerializer(sub_task)
        return Response(serializer.data)

    def put(self, request, pk):
        sub_task = self.get_object(pk)
        serializer = SubTaskDetailSerializer(sub_task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sub_task = self.get_object(pk)
        sub_task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


