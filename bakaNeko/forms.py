from django import forms
from django.forms import ModelForm
from .models import Post, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Creacion de la clase

class formularioPost(ModelForm):
    class Meta:
        model = Post
        fields = ['idPost','fechaPost','tituloPost','descPost','imagenPost','estado','razonPost','usuario']

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']