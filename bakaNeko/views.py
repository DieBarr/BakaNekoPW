from django.shortcuts import render, redirect
from .models import Usuario, Rol, Post, Comentario, Estado, Tipo
from django.contrib import messages
import datetime
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
  
def registrar(request):
    u_nombre = request.POST['nomUsuario']
    u_email = request.POST['correoUsuario']
    u_foto = request.FILES['fotoPerfil']
    u_contrasenia = request.POST['contraUsuario']
    u_repcontra = request.POST['repetirContra']
    rol_u = Rol.objects.get(nombreRol = 'usuario')
    ##regexEmail = "/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/"
    ##regexPassword = "/(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/"

    if (len(u_nombre) < 4 and len(u_nombre) > 12):
        messages.error(request, "El nombre de usuario no es válido (＃`Д´) !")
        return redirect('registro')
    elif u_contrasenia != u_repcontra:
        messages.error(request, "Las contraseñas no coinciden ٩(╬ʘ益ʘ╬)۶ !")
        return redirect('registro')
    ##insert
    Usuario.objects.create(nombreUsuario = u_nombre, email = u_email, fotoUsuario = u_foto, contrasenia = u_contrasenia, rol = rol_u)
    return redirect('registro')

def login(request):
    nombre_l = request.POST['nomLogin']
    contra_l = request.POST['contraLogin']
    try:
        usuario_l = Usuario.objects.get(nombreUsuario = nombre_l)
        if usuario_l.contrasenia == contra_l:
            messages.success(request, "Bienvenido "+usuario_l.nombreUsuario+" ☆*:.｡.o(≧▽≦)o.｡.:*☆!!!")
            return redirect('index')
        else:
            messages.error(request, "La contraseña no es válida (＃`Д´)!!")
            return redirect('registro')
    except:
        messages.error(request, "El usuario no existe, se sugiere crear uno (╬ Ò﹏Ó)")
        return redirect('registro')


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
    tipos = Tipo.objects.all()
    contexto = {"tipo":tipos}
    return render(request, 'bakaNeko/nuevoPost.html', contexto)

def registrarPost(request, user):
    img_p = ""
    fecha_p = datetime.date.today()
    titulo_p = request.POST['asunto']
    desc_p = request.POST['descPost']
    tipo_p = request.POST['tipoSel']
    tipo_p2 = Tipo.objects.get(idTipo = tipo_p)
    usuario_p = Usuario.objects.get(nombreUsuario = user)
    est_p = Estado.objects.get(nombre="activo")
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
            Post.objects.create(fechaPost=fecha_p, tituloPost=titulo_p, descPost=desc_p, estado=est_p, usuario=usuario_p,  tipo=tipo_p)
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