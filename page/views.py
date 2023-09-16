from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# page
@login_required(login_url='login-page')
def dashboard(request):
    
    return render(request, 'pages/dashboard.html')

@login_required(login_url='login-page')
def allProject(request):
    return render(request, 'pages/projects.html')

def _logout(request):
    logout(request)
    return redirect('dashboard')





# Authentications
def register(request):
    
    return render(request, 'authentications/register.html')
    

def login(request):
    
    return render(request, 'authentications/login.html')




# 404 Page
def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)