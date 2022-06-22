from django.urls import path
from api_rest.views import lista_post, control_post, control_users, lista_coment, lista_users
from api_rest.viewsLogin import loginApi

appName = 'api'

urlpatterns = [
    path('lista_post/',lista_post,name="lista_post"),
    path('control_post/<id>',control_post,name="control_post"),
    path('control_users/<userName>', control_users, name="control_usuarios"),
    path('login',loginApi,name="loginApi"),
    path('lista_comentarios', lista_coment, name="lista_coment"),
    path('lista_usuarios/', lista_users, name="lista_usuarios"),
]