# django DB
from django.db import models


# django contrib
from django.contrib.auth.models import User



# Create your models here.

class Tags(models.Model):
    tags = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return self.tags


class Project(models.Model):
    
    STATUS = (
        (1, "developing"),
        (2, "finished"),
        (3, "letter"),
        (4, "for got")
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    desc = models.TextField(default="-")
    status = models.IntegerField(choices=STATUS, default=1)
    
    create_date = models.DateTimeField(auto_now_add=True)
    lasts_edit = models.DateTimeField(auto_created=True, auto_now_add=True)  
    finish_date = models.DateTimeField()
    
    repo = models.URLField()
    
    def __str__(self) -> str:
        return self.name
  
class TaskManagement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.project.name
    
class Task(models.Model):
    
    task_management = models.ForeignKey(TaskManagement, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=128)
    task_desc = models.TextField()
    task_status = models.BooleanField(default=False)
    
    def __str__(self) ->str:
        return self.task_management.project.name

    
   
    
    
    