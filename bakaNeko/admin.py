from django.contrib import admin
from .models import Rol,Usuario,Estado,Post,Comentario 

# Register your models here.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Estado)
admin.site.register(Post)
admin.site.register(Comentario)