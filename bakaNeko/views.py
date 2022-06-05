from django.shortcuts import render, get_object_or_404
from .models import Rol,Usuario,Estado,Post,Comentario 

# Create your views here.
def index(request):
    return render(request,'bakaNeko/index.html')

def secanime(request):
    posts = Post.objects.all()

    datos = {
    'posts' : posts
    }


    return render(request,'bakaNeko/secAnime.html', datos)

def secjuegos(request):
    
    posts = Post.objects.all()

    datos2 = {
    'posts' : posts
    }


    return render(request,'bakaNeko/secVideojuegos.html', datos2)

def registro(request):
    return render(request, 'bakaNeko/sesionRegistro.html')