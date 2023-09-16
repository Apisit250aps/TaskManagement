from django.urls import path

from . import views as api

urlpatterns = [
    # checking
    path('email-exist', api.email_exist, name='check-email'),
    path('username-exist', api.username_exist, name='check-username'),
    
    # authentication
    path('register', api.user_register, name='register-api'),
    path('login', api.user_login, name='login-api'),
    
    
    
    
]
