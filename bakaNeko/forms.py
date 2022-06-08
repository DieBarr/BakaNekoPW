from django import forms


#Este es el formulario del login
class FormLoginUsuario(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id':'loginEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    contrasenia = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'loginPassword',
            'type': 'password',
            'class': 'form-control',
        })
    )








#Este es el formulario de registro
class FormRegisUsuario(forms.Form):
    user_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'signupEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    foto = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id': 'image',
                'type': 'image',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'signupPassword',
                'type': 'password',
                'class': 'form-control'
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control'
            }
        ))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']