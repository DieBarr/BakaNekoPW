from django.shortcuts import render
from .models import Post, Comentario
# Create your views here.
def index(request):
    return render(request,'bakaNeko/index.html')

def lista(request):
    posts = Post.objects.all()
    coments = Comentario.objects.all()
    contexto = {"post":posts, "comentario":coments}
    return render(request, 'bakaNeko/listaPosts.html', contexto)
