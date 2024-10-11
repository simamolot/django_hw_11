from datetime import date

from rest_framework import serializers

from homework_app.models.task import Category
from homework_app.models.task import SubTask, Task


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        read_only_fields = ('created_at',)




class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

    def validate_title(self, data):
        if Category.object.filter(title=data).exists():
            raise serializers.ValidationError('Title already exists')
        return data


    def create(self, validated_data):
        if Category.object.filter(title=validated_data['title']).exists():
            raise serializers.ValidationError('Title already exists')
        return validated_data

    def update(self, instance, validated_data):
        if 'title' in validated_data and instance.title != instance.title:
            if Category.object.filter(title=validated_data['title']).exists():
                raise serializers.ValidationError('Title already exists')

        instance.title = validated_data['title']
        instance.save()
        return instance


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SubTaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']





