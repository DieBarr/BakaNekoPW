from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, get_user_model
from .serializers import PostSerializer, ComSerializer, UserSerializer
from bakaNeko.models import Post, Comentario, Usuario
# Create your views here.

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_post(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def lista_coment(request):
    if request.method == 'GET':
        com = Comentario.objects.all()
        serializer = ComSerializer(com, many=True)
        return Response(serializer.data)

@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def lista_users(request):
    if request.method == 'GET':
        user = get_user_model().objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
@api_view(['GET', 'DELETE', 'PUT'])
def control_users(request):
    try:
        user = get_user_model().objects.get(id = id)

    except get_user_model().DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def control_post(request, id):
    try:
        p = Post.objects.get(idPost = id)

    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(p)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(p, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        p.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)