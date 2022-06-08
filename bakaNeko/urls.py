"""bakaNeko_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import index, lista, registro, verPost, verPerfil, registrarComentario, nuevoPost, registrarPost, secanime, secjuegos, login
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('registro/',registro,name='registro'),
    path('reg', views.signup_view, name='regUser'),
    path('log', views.login_view, name='logUser'),
    path('posts', lista, name="listaPosts"),
    path('posts/<int:id>', verPost, name='verPosts'),
    path('perfil/<int:id>', verPerfil, name='verPerf'),
    path('registrarCom/com_<int:id>_<str:user>', registrarComentario, name='registrarCom'),
    path('nuevoPost/<int:user>', nuevoPost, name="nuevoPost"),
    path('publicar/<int:user>', registrarPost, name="registrarPost"),
    path('secAnime/', secanime, name='secAnime'),
    path('secVideojuegos/', secjuegos, name='secJuegos'),
]
