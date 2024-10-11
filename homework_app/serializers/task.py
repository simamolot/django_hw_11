from rest_framework import serializers

from homework_app.models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline']


data1 = {'title': 'Complete Homework',
         'description': 'Help complete homework',
         'status': '',
         'deadline': ''}

serializer = TaskSerializer(data=data1)
if serializer.is_valid():
    print('Good data', serializer.validated_data)
