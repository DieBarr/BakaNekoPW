from django import forms
from django.forms import ModelForm
from .models import Post

#Creacion de la clase

class formularioPost(ModelForm):
    class Meta:
        model = Post
        fields = ['idPost','fechaPost','tituloPost','descPost','imagenPost','estado','razonPost','usuario']