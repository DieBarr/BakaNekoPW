from django.shortcuts import render, redirect
from .models import Usuario, Rol, Post, Comentario, Estado
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
    return render(request,'bakaNeko/index.html')

def lista(request):
    posts = Post.objects.all()
    coments = Comentario.objects.all()
    contexto = {"post":posts, "comentario":coments}
    return render(request, 'bakaNeko/listaPosts.html', contexto)

def registro(request):
    return render(request,'bakaNeko/registro.html')
  
def registrar(request):
    u_nombre = request.POST['usuario']
    u_email = request.POST['correo']
    u_contrasenia = request.POST['contrasenia']
    u_rol = request.POST['rol']
    rol_u = Rol.objects.get(id_rol = u_rol)
    ##insert
    Usuario.objects.create(nombreUsuario = u_nombre, email = u_email, contrasenia = u_contrasenia, rol = u_rol)
    return redirect('index')

def verPost(request, id):
    postSel = Post.objects.get(idPost = id)
    userSel = Usuario.objects.get(idUsuario = postSel.usuario.idUsuario)
    comSel = Comentario.objects.filter(post = postSel)
    contexto = {
        "post" : postSel,
        "usuario" : userSel,
        "comentario" : comSel
    }

    return render(request, 'bakaNeko/verPost.html', contexto)

def registrarComentario(request, id, user):
    desc_c = request.POST['comment']
    fecha_c = datetime.date.today()
    usuario_c = Usuario.objects.get(idUsuario = user)
    post_c = Post.objects.get(idPost = id)
    est_c = Estado.objects.get(nombre = "activo")

    Comentario.objects.create(fechaCom = fecha_c, usuario = usuario_c, post = post_c, estado = est_c, descCom = desc_c)
    
    messages.success(request, "Comentario creado correctamente felicidades ☆*:.｡.o(≧▽≦)o.｡.:*☆!")

    return redirect('verPosts', id)
