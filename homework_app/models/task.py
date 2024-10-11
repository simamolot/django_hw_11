from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User



STATUSES_CHOICES = [
    ('New', 'New'),
    ('In_progress', 'In_progress'),
    ('Completed', 'Completed'),
    ('Closed', 'Closed'),
    ('Pending', 'Pending'),
    ('Blocked', 'Blocked'),
]

PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ('Very High', 'Very High'),
]

class Task(models.Model):
    title = models.CharField(
        max_length=255, unique=True, validators=[MinLengthValidator(10)]
    )
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUSES_CHOICES, default='New')
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-due_date', '-priority']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class SubTask(models.Model):
    title = models.CharField(
        max_length=255, validators=[MinLengthValidator(10)]
    )
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUSES_CHOICES, default='New')
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-due_date', '-priority']
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'




class Category(models.Model):
   name = models.CharField(max_length=40, unique=True)

   def __str__(self):
       return self.name

   class Meta:
       ordering = ['name']
       verbose_name_plural = 'categories'


