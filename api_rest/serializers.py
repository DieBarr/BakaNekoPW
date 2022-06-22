from rest_framework import serializers
from bakaNeko.models import Post, Comentario, Usuario

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['idPost','fechaPost', 'tituloPost', 'descPost', 'imagenPost', 'estado', 'razonPost', 'usuario', 'tipo']

class ComSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['idCom', 'fechaCom', 'usuario', 'post', 'estado', 'razonCom', 'descCom']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'user_name', 'profile_pic', 'register_date', 'is_staff']