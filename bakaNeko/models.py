from pyexpat import model
from tabnanny import verbose

from django.db import models



# Create your models here.
class Rol(models.Model):
    idRol = models.AutoField(primary_key=True,verbose_name="Codigo rol")
    nombreRol = models.CharField(max_length=30,verbose_name="Nombre rol")

class Tipo(models.Model):
    idTipo = models.AutoField(primary_key=True,verbose_name="Codigo del Tipo")
    nombreTipo = models.CharField(max_length=30,verbose_name="Nombre del Tipo")

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="Codigo de Usuario")
    nombreUsuario = models.CharField(max_length=30, verbose_name="Nombre de Usuario")
    contrasenia = models.CharField(max_length=20, verbose_name="Contraseña del Usuario")
    email = models.EmailField(max_length=30, verbose_name="Correo del Usuario")
    fotoUsuario = models.ImageField(upload_to="fotoPerfiles", null=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_DEFAULT, default="sinRol")


class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True, verbose_name="Codigo de Status")
    nombre = models.CharField(max_length=30, verbose_name="Tipo de status")

class Post(models.Model): 
    idPost = models.AutoField(primary_key=True, verbose_name="Codigo del Post")
    fechaPost = models.DateField(verbose_name="Fecha del Post")
    tituloPost = models.CharField(max_length=150, verbose_name="Titulo del Post")
    descPost = models.CharField(max_length=500, verbose_name="Descripcion del Post")

    imagenPost = models.ImageField(upload_to="imagenPosts", blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    razonPost = models.CharField(max_length=100, null=True, verbose_name="Razon del Baneo")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
class Comentario(models.Model):
    idCom = models.AutoField(primary_key=True, verbose_name="Codigo del Comentario")
    fechaCom = models.DateField(verbose_name="Fecha del comentario")
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_DEFAULT, default="Activo")
    razonCom = models.CharField(max_length=100, null=True, verbose_name="Razon del Baneo")
    descCom = models.CharField(max_length=400, verbose_name="Contenido del comentario")

