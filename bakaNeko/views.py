from django.shortcuts import render, get_object_or_404, redirect
from .models import Rol,Usuario,Estado,Post,Comentario 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
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
    
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
            password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Te has registrado correctamente!")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/sesionRegistro.html', data)

