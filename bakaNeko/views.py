from ast import For
from django.contrib import messages
import datetime
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import FormLoginUsuario, FormRegisUsuario

def login_view(request):
    login_form = FormLoginUsuario(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('contrasenia')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesion correctamente')
            return redirect('index')
        else:
            messages.warning(
                request, 'Usuario o Contrasena invalida')
            return redirect('index')

    messages.error(request, 'Formulario Invalido')
    return redirect('index')


def signup_view(request):
    signup_form = FormRegisUsuario(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        user_name = signup_form.cleaned_data.get('user_name')
        password = signup_form.cleaned_data.get('password')
        try:
            user = get_user_model().objects.create(
                email=email,
                user_name=user_name,
                password=make_password(password),
                rol = Rol.objects.get(idRol = 1)
            )
            login(request, user)
            return redirect('index')

        except Exception as e:
            messages.warning(request, e)
            return JsonResponse({'detail': f'{e}'})
    else:
        messages.warning(request, "Ocurrió un error desconocido")
        return redirect('registro')
        
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def profile_view(request, id):
    usuario = get_user_model().objects.get(id = id)
    return render(request, 'bakaNeko/perfil.html', { "usuario": usuario })

def index(request):
    posts_car = Post.objects.filter(fechaPost = datetime.date.today())
    posts_i = Post.objects.all()
    contexto = {"postCarr":posts_car, 
                "post":posts_i
    }
    return render(request,'bakaNeko/index.html', contexto)

def lista(request):
    posts = Post.objects.all()
    coments = Comentario.objects.all()
    contexto = {"post":posts, "comentario":coments}
    return render(request, 'bakaNeko/listaPosts.html', contexto)

def registro(request):
    return render(request,'bakaNeko/registro.html')
  
def verPost(request, id):
    postSel = Post.objects.get(idPost = id)
    userSel = get_user_model().objects.get(id = postSel.usuario.id)
    comSel = Comentario.objects.filter(post = postSel)
    contexto = {
        "post" : postSel,
        "usuario" : userSel,
        "comentario" : comSel
    }

    return render(request, 'bakaNeko/verPost.html', contexto)

def nuevoPost(request):
    tipos = Tipo.objects.all()
    contexto = {
        "tipo":tipos,
    }
    return render(request, 'bakaNeko/nuevoPost.html', contexto)

def registrarPost(request, user):
    img_p = ""
    fecha_p = datetime.date.today()
    titulo_p = request.POST['asunto']
    desc_p = request.POST['descPost']
    tipo_p = request.POST['tipoSel']
    tipo_p2 = Tipo.objects.get(idTipo = tipo_p)
    usuario_p = get_user_model().objects.get(user_name = user)
    est_p = Estado.objects.get(nombre="activo")
    ##request.session['user'] = usuario_p
    if len(titulo_p) > 100:
        messages.error(request, "Error: El Asunto no puede tener más de 100 caracteres (╬ Ò﹏Ó)!")
        return redirect('nuevoPost')
    else:
        try:
            img_p = request.FILES['imgPost']
            Post.objects.create(fechaPost=fecha_p, tituloPost=titulo_p, descPost=desc_p, imagenPost=img_p, estado=est_p, usuario=usuario_p, tipo=tipo_p2)
            messages.error(request, "Post creado correctamente felicidades ☆*:.｡.o(≧▽≦)o.｡.:*☆!")
            return redirect('index')
        except:
            Post.objects.create(fechaPost=fecha_p, tituloPost=titulo_p, descPost=desc_p, estado=est_p, usuario=usuario_p,  tipo=tipo_p2)
            messages.success(request, "Post creado correctamente felicidades ☆*:.｡.o(≧▽≦)o.｡.:*☆!")
            return redirect('index')

def registrarComentario(request, id, user):
    desc_c = request.POST['comment']
    fecha_c = datetime.date.today()
    usuario_c = get_user_model().objects.get(id = user)
    post_c = Post.objects.get(idPost = id)
    est_c = Estado.objects.get(nombre = "activo")

    Comentario.objects.create(fechaCom = fecha_c, usuario = usuario_c, post = post_c, estado = est_c, descCom = desc_c)
    
    messages.success(request, "Comentario creado correctamente felicidades ☆*:.｡.o(≧▽≦)o.｡.:*☆!")

    return redirect('verPosts', id)

def secanime(request):
    posts = Post.objects.filter(tipo_id = 1)

    datos = {
    'posts' : posts
    }
    return render(request,'bakaNeko/secAnime.html', datos)

def secjuegos(request):
    
    posts = Post.objects.filter(tipo_id = 2)

    datos2 = {
    'posts' : posts
    }


    return render(request,'bakaNeko/secVideojuegos.html', datos2)