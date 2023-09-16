# django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

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
