from tabnanny import verbose
from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="Codigo de Usuario")
    nombreUsuario = models.CharField(max_length=30, verbose_name="Nombre de Usuario")
    contrasenia = models.CharField(max_length=20, verbose_name="Contraseña del Usuario")
    email = models.EmailField(max_length=30, verbose_name="Correo del Usuario")

class Perfil(models.Model):
    foto_perfil = models.ImageField(upload_to="fotoPerfiles", null=True)
    pais_perfil = models.CharField(max_length=20, verbose_name="Pais del Usuario")
    tipo_user = models.CharField(max_length=5, verbose_name="Tipo de Usuario") # Admin | Comun | Mod
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)