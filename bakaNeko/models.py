from tabnanny import verbose
from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="Codigo de Usuario")
    nombreUsuario = models.CharField(max_length=30, verbose_name="Nombre de Usuario")
    contrasenia = models.CharField(max_length=20, verbose_name="Contraseña del Usuario")
    email = models.EmailField(max_length=30, verbose_name="Correo del Usuario")
    foto_perfil = models.ImageField(upload_to="fotoPerfiles", null=True)
    tipo_user = models.CharField(max_length=5, verbose_name="Tipo de Usuario") # Admin | Comun | Mod

class Estado(models.Model):
    idStatus = models.AutoField(primary_key=True, verbose_name="Codigo de Status")
    nombre = models.CharField(max_length=30, verbose_name="Tipo de status")
class Post(models.Model):
    idPost = models.AutoField(primary_key=True, verbose_name="Codigo del Post")
    fechaPost = models.DateField(verbose_name="Fecha del Post")
    tituloPost = models.CharField(max_length=150, verbose_name="Titulo del Post")
    descPost = models.CharField(max_length=500, verbose_name="Descripcion del Post")
    imagenPost = models.ImageField(upload_to="imagenPosts", null=True)
    estado = models.ForeignKey(Estado)
    razonPost = models.CharField(max_length=100, null=True, verbose_name="Razon del Baneo")
    usuario = models.ForeignKey(Usuario)

class Comentario(models.Model):
    idCom = models.AutoField(primary_key=True, verbose_name="Codigo del Comentario")
    fechaCom = models.DateField(verbose_name="Fecha del comentario")
    usuario = models.ForeignKey(Usuario)
    post = models.ForeignKey(Post)
    estado = models.ForeignKey(Estado)
    razonCom = models.CharField(max_length=100, null=True, verbose_name="Razon del Baneo")
    descCom = models.CharField(max_length=400, verbose_name="Contenido del comentario")
