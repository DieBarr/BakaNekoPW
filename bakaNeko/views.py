from django.shortcuts import render
from .forms import formularioPost

# Create your views here.
def index(request):
    return render(request,'bakaNeko/index.html')

def form_post(request):
    return render(request,'bakaNeko/nuevoPost.html')


#***formulario bakaneko***
def form_post(request):
    #El view entrega el formulario al template
    datos = {
        'form' : formularioPost()
    }
    #Se verifica que sea POST la petición  y se rescatan los datos
    if request.method == 'POST':
        #Se recuperan los datos y se ingresan a formulario
        formulario = formularioPost(request.POST)
        #Se valida el formulario
        if formulario.is_valid:
            #Se guardan los datos en la base de datos
            formulario.save()
            datos['mensaje'] = "Post enviado correctamente"

    return render(request,'bakaNeko/nuevoPost.html', datos)

