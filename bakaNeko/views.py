from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'bakaNeko/index.html')



def listado(request):
    posts = Mascota.objects.all() #generando un select * from de la tabla posts
    contexto = {"mascota":mascotas}
    return render(request,'core/ListadoMascotas.html',contexto)