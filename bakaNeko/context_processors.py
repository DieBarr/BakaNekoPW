from .forms import FormLoginUsuario, FormRegisUsuario


def login_form(request):
    login_form = FormLoginUsuario()
    signup_form = FormRegisUsuario()
    return {
        'loginForm': login_form,
        'signupForm': signup_form
    }