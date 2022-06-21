<<<<<<< HEAD
from ast import For
=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import Usuario, Rol, Post, Comentario, Estado, Tipo
>>>>>>> origin/main
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
            return redirect('registro')

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

def registro(request):
    return render(request,'bakaNeko/registro.html')
  
<<<<<<< HEAD
=======
def registrarUsuario(request):
    nom_r = request.POST['nomUsuario']
    email_r = request.POST['correoUsuario']

    ## condicional de foto por default
    try:
        foto_r = request.FILES['fotoPerfil']
    except:
        foto_r = 'fotoPerfiles/default.jpg'
    ##
    contra_r = request.POST['contraUsuario']
    rol_r = Rol.objects.get(nombreRol = 'usuario')
    ## Condicionales
    if contra_r != request.POST['repetirContra']:
        messages.warning(request, "Las contraseñas no coinciden!")
        return redirect('registro')
    try:
        if Usuario.objects.get(nombreUsuario = nom_r):
            messages.warning(request, "El usuario ya existe!!")
            return redirect('registro')
    except:
        try:
            if Usuario.objects.get(email = email_r):
                messages.warning(request, "El usuario ya existe!!")
                return redirect('registro')
        except:
            Usuario.objects.create(nombreUsuario = nom_r, email = email_r, fotoUsuario = foto_r, contrasenia = contra_r, rol = rol_r)
            messages.success(request, "Se ha registrado correctamente!")
            return redirect('registro')

def iniciarSesion(request):
    nom_l = request.POST['nomLogin']
    contra_l = request.POST['contraLogin']
    ## autenticacion
    try:
        usuario = Usuario.objects.get(nombreUsuario = nom_l)
        if usuario.contrasenia == contra_l:
            login(request, usuario)
            messages.success(request, "Inicio de sesión exitoso!!")
            return redirect('index')
        else:
            messages.warning(request, "Contraseña invalida!!")
            return redirect('registro')
    except:
        messages.warning(request, "Usuario o contraseña invalidos")
        return redirect('registro')
    return redirect('registro')

def verPerfil(request, id):
    userPerf = Usuario.objects.get(idUsuario = id)
    postPerf = Post.objects.filter(usuario_id = id)
    contexto ={
        "usuario": userPerf,
        "post": postPerf
    }
    return render(request, 'bakaNeko/perfil.html', contexto)
    
>>>>>>> origin/main
def verPost(request, id):
    postSel = Post.objects.get(idPost = id)
    userSel = get_user_model().objects.get(id = postSel.usuario.id)
    comSel = Comentario.objects.filter(post = postSel)
<<<<<<< HEAD
=======
    userAct = Usuario.objects.get(idUsuario = 3)
>>>>>>> origin/main
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
