<<<<<<< HEAD
from django.shortcuts import render
from .models import Post, Comentario
=======
from django.shortcuts import render, redirect
from .models import Usuario, Rol
from django.contrib import messages

>>>>>>> main
# Create your views here.
def index(request):
    return render(request,'bakaNeko/index.html')

<<<<<<< HEAD
def lista(request):
    posts = Post.objects.all()
    coments = Comentario.objects.all()
    contexto = {"post":posts, "comentario":coments}
    return render(request, 'bakaNeko/listaPosts.html', contexto)
=======

def registro(request):
    return render(request,'bakaNeko/registro.html')
  
def registrar(request):
    u_nombre = request.POST['usuario']
    u_email = request.POST['correo']
    u_contrasenia = request.POS['contrasenia']
    u_rol = request.POST['rol']
    rol_u = Rol.objects.get(id_rol = u_rol)
    ##insert
    Usuario.objects.create(nombreUsuario = u_nombre, email = u_email, contrasenia = u_contrasenia, rol = u_rol)
    return redirect('index')
>>>>>>> main
