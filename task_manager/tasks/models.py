from django import forms
from django.contrib.auth.models import User
from django.db import models

from task_manager.statuses.models import Status


# Create your models here.
class Task(models.Model):
    date_of_creation = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='authored_tasks')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='processing_tasks', blank=True, null=True)
    description = models.TextField(blank=True)