from django.urls import path

from . import views

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/<int:id>', views.profile_view, name='profile'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]