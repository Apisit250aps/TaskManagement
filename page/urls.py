from django.urls import path

from . import views

urlpatterns = [
    # page
    path('', views.dashboard, name='dashboard'),
    path('projects', views.allProject, name='project-all'),
    
    # authentication url
    path('register/', views.register, name='register-page'),
    path('login/', views.login, name='login-page'),
    path('logout/', views._logout, name='logout'),
    
    
]


