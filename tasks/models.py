from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('WIP', 'Work In Progress'),
        ('DONE', 'Done'),
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    planned_hours = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='TODO')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return f'Comment by {self.user} on {self.task}'


class TaskWorked(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.user} worked {self.hours}h on {self.task}'
