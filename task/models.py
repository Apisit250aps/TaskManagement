# django DB
from django.db import models


# django contrib
from django.contrib.auth.models import User


# Create your models here.


STATUS = (
        (1, "new"),
        (2, "in progress"),
        (3, "completed"),
    )

class Project(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    desc = models.TextField(default="-")
    status = models.IntegerField(choices=STATUS, default=1)
    budget = models.DecimalField(max_digits=9, decimal_places=2)
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField() 
    
    repo = models.URLField()
    
    def __str__(self) -> str:
        return self.name

class TaskManagement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.project.name
    
class Task(models.Model):
    
    task_management = models.ForeignKey(TaskManagement, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=128)
    task_desc = models.TextField()
    task_status = models.BooleanField(default=False)
    
    start_date = models.DateTimeField(  null=True)
    end_date = models.DateTimeField(default=None, null=True)
    
    def __str__(self) ->str:
        return self.task_management.project.name

    
   
    
    
    