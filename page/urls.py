from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # authentication url
    path('register/', views.register, name='register-page'),
    
]


