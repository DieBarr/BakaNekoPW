from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def loginApi(request):
    data = JSONParser().parse(request)

    usuario = data['username']
    clave = data['password']
    try:
        user1 = get_user_model().objects.get(user_name = usuario)
    except get_user_model.DoesNotExist:
        return Response("Usuario Incorrecto")
    #Validación contraseña
    pass_valida = check_password(clave, user1.password)

    if not pass_valida:
        return Response("Contraseña Incorrecta")
    #Creación o recuperacion del token
    token, created = Token.objects.get_or_create(user = user1)
    #print token
    return Response(token.key)