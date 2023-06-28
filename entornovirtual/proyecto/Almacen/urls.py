from django.urls import path
from .import views

urlpatterns=[

    #login
    path("",views.login_usuario),
    path("RegistroUsuario",views.registrar_usuario),

    path("Inicio",views.index)
    ]