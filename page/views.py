from django.shortcuts import render

# Create your views here.

def dashboard(request):
    
    return render(request, 'pages/base.html')



# Authentications

def register(request):
    
    return render(request, 'pages/authentications/auth-register-basic.html')
    
    