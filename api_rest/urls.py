from django.urls import path
from api_rest.views import lista_post, control_post
from api_rest.viewsLogin import loginApi

appName = 'api'

urlpatterns = [
    path('lista_post/',lista_post,name="lista_post"),
    path('control_post/<id>',control_post,name="control_post"),
    path('login',loginApi,name="loginApi"),
]