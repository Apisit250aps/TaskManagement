from django.contrib import admin

from . import models

# Register your models here.



@admin.register(models.Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'status',
        'start_date',
        'end_date',
        'user'
    ]
    
