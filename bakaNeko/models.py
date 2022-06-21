from pyexpat import model
from tabnanny import verbose
from django.conf import settings
from django.db import models
import random
import string

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.urls import reverse
import datetime
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, **other_fields):
        rol_admin = Rol.objects.get(idRol=1)
        other_fields.setdefault('rol', rol_admin)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        if other_fields.get('rol') is not rol_admin:
            raise ValueError(
                'Superuser must be assigned to rol=1.')

        return self.create_user(email, user_name, password, **other_fields)

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True,verbose_name="Codigo rol")
    nombreRol = models.CharField(max_length=30,verbose_name="Nombre rol")


class Tipo(models.Model):
    idTipo = models.AutoField(primary_key=True,verbose_name="Codigo del Tipo")
    nombreTipo = models.CharField(max_length=30,verbose_name="Nombre del Tipo")

class Usuario(AbstractBaseUser, PermissionsMixin):
    #Rol.objects.create(nombreRol='admin')
    #Rol.objects.create(nombreRol='usuario')
    email = models.EmailField(unique=True, verbose_name="Correo del Usuario")
    user_name = models.CharField(max_length=100, verbose_name="Nombre de Usuario")
    profile_pic = models.ImageField(
        upload_to='fotoPerfiles/', default='fotoPerfiles/default.jpg', verbose_name="Foto del Usuario")
    slug = models.SlugField(max_length=255, unique=True)

    register_date = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    
    rol = models.ForeignKey(Rol, on_delete=models.SET_DEFAULT, default=0)
    def __str__(self):
        return f'{self.user_name}'

    def get_absolute_url(self):
        return reverse('user_detail', args=[self.slug])

    def count_posts(self):
        return Post.objects.filter(author=self).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.email)
        super(Usuario, self).save(*args, **kwargs)


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
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)

class Comentario(models.Model):
    idCom = models.AutoField(primary_key=True, verbose_name="Codigo del Comentario")
    fechaCom = models.DateField(verbose_name="Fecha del comentario")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_DEFAULT, default="Activo")
    razonCom = models.CharField(max_length=100, null=True, verbose_name="Razon del Baneo")
    descCom = models.CharField(max_length=400, verbose_name="Contenido del comentario")
