from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Task, Comment, TaskWorked
from django.contrib.auth.models import User
from .serializers import TaskSerializer, CommentSerializer, TaskWorkedSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'owner']
    search_fields = ['name', 'description']
    ordering_fields = ['planned_hours']


    @action(detail=True, methods=['get'])
    def worked_hours(self, request, pk=None):
        task = self.get_object()
        total_worked = TaskWorked.objects.filter(task=task).aggregate(total_hours=Sum('hours'))['total_hours'] or 0
        difference = task.planned_hours - total_worked
        return Response({"total_worked_hours": total_worked, "difference": difference})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task', 'user']


class TaskWorkedViewSet(viewsets.ModelViewSet):
    queryset = TaskWorked.objects.all().order_by('id')
    serializer_class = TaskWorkedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task', 'user']

    @action(detail=False, methods=['get'])
    def total_hours_by_user(self, request):
        total_hours = TaskWorked.objects.values('user').annotate(total_hours=Sum('hours')).order_by('user')
        return Response(total_hours)

