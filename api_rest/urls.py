from django.urls import path
from api_rest.views import lista_post, control_post, control_comentario, control_usuario, lista_comentario, lista_usuario
from api_rest.viewsLogin import loginApi

appName = 'api'

urlpatterns = [
    path('lista_post/',lista_post,name="lista_post"),
    path('lista_comentario/',lista_comentario,name="lista_comentario"),
    path('lista_usuario/',lista_usuario,name="lista_usuario"),
    path('control_post/<id>',control_post,name="control_post"),
    path('login',loginApi,name="loginApi"),
    path('control_comentario/<id>',control_comentario,name="control_comentario"),
    path('control_usuario/<id>',control_usuario,name="control_usuario"),
]
