from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login-page')
def dashboard(request):
    
    return render(request, 'pages/base.html')



# Authentications

def register(request):
    
    return render(request, 'pages/authentications/register.html')
    

def login(request):
    
    return render(request, 'pages/authentications/login.html')
    