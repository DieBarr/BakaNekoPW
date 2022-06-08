from ast import For
from django.shortcuts import get_object_or_404, render, redirect
from .models import Usuario, Rol, Post, Comentario, Estado, Tipo
from django.contrib import messages
import datetime

def index(request):
    posts_car = Post.objects.filter(fechaPost = datetime.date.today())
    posts_i = Post.objects.all()
    contexto = {"postCarr":posts_car, 
                "post":posts_i,
                "user":""
    }
    return render(request,'bakaNeko/index.html', contexto)

def lista(request):
    posts = Post.objects.all()
    coments = Comentario.objects.all()
    contexto = {"post":posts, "comentario":coments}
    return render(request, 'bakaNeko/listaPosts.html', contexto)

def registro(request):
    return render(request,'bakaNeko/registro.html')
  
def registrarUsuario(request):
    pass
def login(request):
    pass

def verPerfil(request, id):
    userPerf = Usuario.objects.get(idUsuario = id)
    postPerf = Post.objects.filter(usuario_id = id)
    contexto ={
        "usuario": userPerf,
        "post": postPerf
    }
    return render(request, 'bakaNeko/perfil.html', contexto)
    
def verPost(request, id):
    postSel = Post.objects.get(idPost = id)
    userSel = Usuario.objects.get(idUsuario = postSel.usuario.idUsuario)
    comSel = Comentario.objects.filter(post = postSel)
    userAct = Usuario.objects.get(idUsuario = 4)
    contexto = {
        "post" : postSel,
        "usuario" : userSel,
        "comentario" : comSel,
        "user":userAct
    }

    return render(request, 'bakaNeko/verPost.html', contexto)

def nuevoPost(request, user):
    usuario_p = Usuario.objects.get(idUsuario = user)
    tipos = Tipo.objects.all()
    contexto = {
        "tipo":tipos,
        "user":usuario_p
    }
    return render(request, 'bakaNeko/nuevoPost.html', contexto)

def registrarPost(request, user):
    img_p = ""
    fecha_p = datetime.date.today()
    titulo_p = request.POST['asunto']
    desc_p = request.POST['descPost']
    tipo_p = request.POST['tipoSel']
    tipo_p2 = Tipo.objects.get(idTipo = tipo_p)
    usuario_p = Usuario.objects.get(idUsuario = user)
    est_p = Estado.objects.get(nombre="activo")
    request.session['user'] = usuario_p
    if len(titulo_p) > 100:
        messages.error(request, "Error: El Asunto no puede tener más de 100 caracteres (╬ Ò﹏Ó)!")
        return redirect('nuevoPost', usuario_p)
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
    usuario_c = Usuario.objects.get(idUsuario = user)
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