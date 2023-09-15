# django
from django.db import models
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
    
    repo = models.URLField()
    
    
    
    
    
    