from rest_framework import serializers
from bakaNeko.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['idPost','fechaPost', 'tituloPost', 'descPost', 'imagenPost', 'estado', 'razonPost', 'usuario', 'tipo']