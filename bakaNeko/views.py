from ast import For
from django.shortcuts import get_object_or_404, render, redirect
from .models import Usuario, Rol, Post, Comentario, Estado
from django.contrib import messages
import datetime
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from .forms import FormLoginUsuario, FormRegisUsuario
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

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
        user_name = signup_form.cleaned_data.get('nombreUsuario')
        foto = signup_form.cleaned_data.get('fotoUsuario')
        password = signup_form.cleaned_data.get('contrasenia')
        try:
            user = get_user_model().objects.create(
                email=email,
                user_name=user_name,
                foto=foto,
                password=make_password(password),
                is_active=True
            )
            login(request, user)
            return redirect('index')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def profile_view(request):
    return render(request, 'bakaNeko/perfil.html')


"""def user_detail(request, slug):
    user = get_object_or_404(get_user_model(), slug=slug)
    is_follower = False
    try:
        if user.is_follower(request.user):
            is_follower = True
    except:
        messages.warning(
            request, 'Debes Iniciar sesion para mas funcionalidades')

    return render(request, 'user/user_detail.html', {'user_detail': user, "is_follower": is_follower})
"""






def index(request):

    posts_car = Post.objects.filter(fechaPost = datetime.date.today())
    posts_i = Post.objects.all()
    contexto = {"postCarr":posts_car, "post":posts_i}
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
    userSel = Usuario.objects.get(idUsuario = postSel.usuario.idUsuario)
    comSel = Comentario.objects.filter(post = postSel)
    contexto = {
        "post" : postSel,
        "usuario" : userSel,
        "comentario" : comSel
    }

    return render(request, 'bakaNeko/verPost.html', contexto)

def nuevoPost(request):
    return render(request, 'bakaNeko/nuevoPost.html')

def registrarPost(request, user):
    img_p = ""
    fecha_p = datetime.date.today()
    titulo_p = request.POST['asunto']
    desc_p = request.POST['descPost']
    if len(titulo_p) > 100:
        messages.error(request, "Error: El Asunto no puede tener más de 100 caracteres (╬ Ò﹏Ó)!")
        return redirect('nuevoPost')
    else:
        try:
            img_p = request.FILES['imgPost']
            usuario_p = Usuario.objects.get(nombreUsuario = user)
            est_p = Estado.objects.get(nombre="activo")
            Post.objects.create(fechaPost=fecha_p, tituloPost=titulo_p, descPost=desc_p, imagenPost=img_p, estado=est_p, usuario=usuario_p)
            messages.error(request, "Post creado correctamente felicidades ☆*:.｡.o(≧▽≦)o.｡.:*☆!")
            return redirect('index')
        except:
            usuario_p = Usuario.objects.get(nombreUsuario = user)
            est_p = Estado.objects.get(nombre="activo")
            Post.objects.create(fechaPost=fecha_p, tituloPost=titulo_p, descPost=desc_p, estado=est_p, usuario=usuario_p)
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

def secanimeAdm(request):
    posts = Post.objects.all()

    datos = {
    'posts' : posts
    }
    return render(request,'bakaNeko/Admin/secAnimeAdm.html', datos)

def eliminarPost(request, id):

    post1 = Post.objects.get(idPost=id)
    post1.delete()
    messages.success(request, 'Post eliminado correctamente')

    return redirect('index')

def usuarioAdm(request, id):

    user = Usuario.objects.get(idUsuario=id)
    user.delete()
    messages.success(request, 'Usuario Baneado')
    return redirect('index')
