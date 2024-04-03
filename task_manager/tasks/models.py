from django.db import models

# Create your models here.
class Task(models.Model):
    #date_of_creation = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)