from rest_framework import serializers
from .models import Task, Comment, TaskWorked


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TaskWorkedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskWorked
        fields = '__all__'
