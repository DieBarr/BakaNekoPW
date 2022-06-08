from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FormLoginUsuario, FormRegisUsuario

def login_view(request):
    login_form = FormLoginUsuario(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesion correctamente')
            return redirect('bakaNeko:index')
        else:
            messages.warning(
                request, 'Usuario o Contrasena invalida')
            return redirect('bakaNeko:registro')

    messages.error(request, 'Formulario Invalido')
    return redirect('bakaNeko:index')


def signup_view(request):
    signup_form = FormRegisUsuario(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        user_name = signup_form.cleaned_data.get('user_name')
        profile_pic = signup_form.cleaned_data.get('profile_pic')
        password = signup_form.cleaned_data.get('password')
        try:
            user = get_user_model().objects.create(
                email=email,
                user_name=user_name,
                profile_pic=profile_pic,
                password=make_password(password),
                is_active=True
            )
            login(request, user)
            return redirect('bakaNeko:index')

        except Exception as e:
            messages.warning(request, e)
            return JsonResponse({'detail': f'{e}'})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def profile_view(request):
    return render(request, 'bakaNeko/perfil.html')


def user_detail(request, slug):
    user_detail = get_object_or_404(get_user_model(), slug=slug)
    if not request.user.is_authenticated:
        messages.warning(request, 'Debes Iniciar sesion para mas funcionalidades')

    return render(request, 'bakaNeko/perfil.html', {'usuario': user_detail})

@login_required(login_url='bakaNeko:index')
def follow(request, slug):
    to_follow = get_object_or_404(get_user_model(), slug=slug)
    if to_follow.is_follower(request.user):
        to_follow.followers.remove(request.user)
    else:
        to_follow.followers.add(request.user)
    to_follow.save
    return redirect(to_follow)