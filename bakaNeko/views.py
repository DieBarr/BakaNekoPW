from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'bakaNeko/index.html')

def perfil(request):
    return render(request, 'bakaNeko/perfil.html')