# django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# rest_framework
from rest_framework import status as http_status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


# app
from . import models

# Create your views here.


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def email_exist(request):
    email = request.data['email']
    is_exist = User.objects.filter(email=email).count() == 0

    return Response(
        {
            "status": is_exist
        }
    )


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def username_exist(request):
    username = request.data['username']
    is_exist = User.objects.filter(username=username).count() == 0

    return Response(
        {
            "status": is_exist
        }
    )


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def user_register(request):
    status = True
    message = ""

    username = request.data['username']
    email = request.data['email']
    password = request.data['password']

    username_isValid = User.objects.filter(username=username).count() == 0
    email_isValid = User.objects.filter(email=email).count() == 0

    if username_isValid and email_isValid:

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        if user:
            status = True
            message = "Successfully!"
        else:
            status = False
            message = "Somethings is Error!"

    else:

        status = False

        if not username_isValid:
            message = "username is exist!"

        if not email_isValid:
            message = "email is exist!"

    return Response(
        {
            "status": status,
            "message": message
        }
    )


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def user_login(request):
    status = False
    msg = ''

    username = request.data['username']
    password = request.data['password']

    try:
        username = User.objects.get(username=username).username
    except:
        username = User.objects.get(email=username).username

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:
        if user.is_active:
            status = True
            msg = 'user is logined'
            login(request, user)
        else:
            status = False
            msg = 'Currently, This user is not active'
    else:
        status = False
        msg = 'Error wrong username/password'

    return Response(
        {
            'status': status,
            'message': msg
        }

    )
