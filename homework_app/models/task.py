from datetime import timedelta, datetime

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    STATUS_CHOICES = (
        ('', 'Не выбрано'),
        ('new', 'Новый'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершен'),
    )
    status = models.BooleanField(choices=STATUS_CHOICES, default='')
    deadline = models.DateTimeField(datetime.now() + timedelta(days=3))

